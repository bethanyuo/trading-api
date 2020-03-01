const ethers = require("ethers");

// 1) New Wallet by Private Key

function createWalletFromPrivateKey(privateKey) {
    return new ethers.Wallet(privateKey);
}

let privateKey = "0x495d5c34c912291807c25d5e8300d20b749f6be44a178d5c50f167d495f3315a";

console.log(createWalletFromPrivateKey(privateKey));

console.log();

// 2) New Randome wallet

function createRandomWallet() {
    return new ethers.Wallet.createRandom();
}

console.log(createRandomWallet());

console.log();

// 3) Save Wallet as JSON

function saveWalletToJSON(wallet, password) {
    return wallet
        .encrypt(password)
        .then(console.log);
}

let wallet = createWalletFromPrivateKey(privateKey);
let password = "p@$$w0rd~3";

saveWalletToJSON(wallet, password);

console.log();

// 4) Load Wallet from JSON

function saveWalletToJSON(wallet, password) {
  return wallet.encrypt(password);
}

async function getWalletFromEncryptedJSON(json, password) {
    return ethers.Wallet.fromEncryptedJson(json, password);
}

(async function() {
    let privateKey = "0x495d5c34c912291807c25d5e8300d20b749f6be44a178d5c50f167d495f3315a";
    let wallet = createWalletFromPrivateKey(privateKey);
    let password = "p@$$w0rd~3";
    let json = await saveWalletToJSON(wallet, password);
    console.log(json);
    let decryptedWallet = await getWalletFromEncryptedJSON(json, password);
    console.log(decryptedWallet);
})();

console.log();

// 5) Sign a transaction

async function signTransaction(wallet, toAddress, value) {
    let transaction = {
        nonce: 0,
        gasLimit: 21000,
        gasPrice: ethers.utils.bigNumberify("2000000000"),
        to: toAddress,
        value: ethers.utils.parseEther(value),
        data: "0x"
    };
    return wallet.sign(transaction);
    }

(async () => {
    let privateKey = "0x495d5c34c912291807c25d5e8300d20b749f6be44a178d5c50f167d495f3315a";
    let wallet = createWalletFromPrivateKey(privateKey);
    let toAddress = "0x7725f560672A512e0d6aDFE7a761F0DbD8336aA7";
    let etherValue = "1";

    let signedTransaction = await signTransaction(wallet, toAddress, etherValue);
    console.log("Signed Transaction:\n" + signedTransaction);
})();

console.log();
