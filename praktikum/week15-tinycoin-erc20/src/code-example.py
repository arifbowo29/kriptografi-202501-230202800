// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol"; // Opsional: untuk kontrol akses

contract TinyCoin is ERC20, Ownable { // Ownable ditambahkan untuk contoh
    constructor(uint256 initialSupply) ERC20("TinyCoin", "TNC") {
        // Mint initialSupply token kepada deployer kontrak (msg.sender)
        _mint(msg.sender, initialSupply);
    }

    // Fungsi tambahan (opsional) - hanya pemilik yang bisa mint lebih banyak token
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    // Fungsi untuk membakar token (mengurangi suplai)
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    // Fungsi untuk mengizinkan alamat lain membelanjakan token atas nama Anda
    // Overrides ERC20 approve untuk menambah event log
    function approve(address spender, uint256 amount) public override returns (bool) {
        bool success = super.approve(spender, amount);
        emit Approval(msg.sender, spender, amount); // Pastikan event dicatat
        return success;
    }
}
