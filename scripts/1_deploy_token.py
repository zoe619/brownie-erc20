from brownie import OurToken, config, network
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(10000000, "ether")

def deploy_token():
    account = get_account()
    ourToken = OurToken.deploy(initial_supply, {"from": account},
     publish_source= config["networks"][network.show_active()].get('verify', False)
    )
    print(ourToken.name())

def main():
    deploy_token()