#![no_std]

elrond_wasm::imports!();

#[elrond_wasm::contract]
pub trait PingPong {
     /// Necessary configuration when deploying:
    /// `normal_search` - the exact amount that needs to be sent when `ping`-ing.  
    /// `duration_in_seconds` - how much time (in seconds) until `pong` can be called after the initial `ping` call  
    /// `token_id` - Optional. The Token Identifier of the token that is going to be used. Default is "EGLD".
    #[init]
    fn init(&self, min_amount: BigUint, duration_in_seconds: u64, opt_token_id: OptionalValue<EgldOrEsdtTokenIdentifier>) {
        require!(min_amount > 0, "Amount cannot be set to zero");
        self.paymentAmount().set(&min_amount);

        require!(
            duration_in_seconds > 0,
            "Duration in seconds cannot be set to zero"
        );
        self.duration_in_seconds().set(&duration_in_seconds);

        let token_id = match opt_token_id {
            OptionalValue::Some(t) => t,
            OptionalValue::None => EgldOrEsdtTokenIdentifier::egld(),
        };
        self.accepted_payment_token_id().set(&token_id);
    }

    """
    The search function is an endpoint of the contract, which means it can be called 
    by external users. It is marked as payable, which means it can receive 
    a payment in the form of a token transfer
    """
    // endpoints
    #[payable("*")] 
    #[endpoint]
    fn search(&self) {
        let (payment_token, payment_amount) = self.call_value().egld_or_single_fungible_esdt();
        require!(
            payment_token == self.accepted_payment_token_id().get(),
            "Invalid payment token"
        );
        require!(
            payment_amount >= self.paymentAmount().get(),
            "The payment amount must be match your type of research"
        );

        let caller = self.blockchain().get_caller();
        let current_block_timestamp = self.blockchain().get_block_timestamp();

        self.user_search(&caller).set(&current_block_timestamp);
    }
    """
    The remove_user function is also an endpoint, but it is marked with the only_owner attribute, 
    which means it can only be called by the contract's owner. 
    It has a single argument, address, which is the address of a user. 
    The function checks that the user has not paid, and if they have not, it clears 
    their search timestamp from the contract's storage.
    """
    #[only_owner]
    #[endpoint]
    fn remove_user(&self, address: &ManagedAddress) {

        require!(!self.did_user_paid(address), "Not paid yet");
        self.user_search(address).clear();
    }

    """
    The did_user_paid function is a view function, which means it can be called
    to read the contract's storage but cannot modify it. 
    It takes an address as an argument and returns a boolean indicating 
    whether the user at that address has paid.
    """
    // views
    #[view(didUserPaid)]
    fn did_user_paid(&self, address: &ManagedAddress) -> bool {
        !self.user_search(address).is_empty()
    }

    // storage
    #[view(getAcceptedPaymentToken)]
    #[storage_mapper("acceptedPaymentTokenId")]
    fn accepted_payment_token_id(&self) -> SingleValueMapper<EgldOrEsdtTokenIdentifier>;

    #[view(getUserSearch)]
    #[storage_mapper("userSearch")]
    fn user_search(&self, address: &ManagedAddress) -> SingleValueMapper<u64>;

    #[view(getPaymentMethod)]
    #[storage_mapper("paymentMethod")]
    fn paymentAmount(&self) -> SingleValueMapper<BigUint>;

    #[view(getDurationTimestamp)]
    #[storage_mapper("durationInSeconds")]
    fn duration_in_seconds(&self) -> SingleValueMapper<u64>;
}