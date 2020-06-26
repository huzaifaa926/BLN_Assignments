pragma solidity 0.4.25;

contract vulnerable
{
    mapping(address => uint256) balances;
    
    function withdraw() external
    {
        balances[msg.sender] = 0;
        uint256 amount = balances[msg.sender];
        require(msg.sender.call.value(amount)());
    }
}

contract malicious
{
    vulnerable public vul = vulnerable(0x0);
    function () public payable
    {
        vul.withdraw();
    }
    
}
