# Hoodi Testnet Deployments

## Core Contracts

| Name                          | Proxy | Implementation | Notes |
| ----------------------------- | ----- | -------------- | ----- |
| PufferVault (pufETH)          | [0xd4A57B33bB84903e7B180f885bb64a2a8b140D85](https://hoodi.etherscan.io/address/0xd4A57B33bB84903e7B180f885bb64a2a8b140D85) | [0xb8405eff81b9227a08e47b094f364bee0148c1e4](https://hoodi.etherscan.io/address/0xb8405eff81b9227a08e47b094f364bee0148c1e4) | Deployed via DeployPufETH |
| AccessManager                 | - | [0x74Cec4ACf425458c9FD1c792Ed2DE6e2339F7b59](https://hoodi.etherscan.io/address/0x74Cec4ACf425458c9FD1c792Ed2DE6e2339F7b59) | Deployed via DeployPufETH |
| GuardianModule                | - | [0x711d5f6c1fa2E6dC11eD60Aa420647c8156DFd73](https://hoodi.etherscan.io/address/0x711d5f6c1fa2E6dC11eD60Aa420647c8156DFd73) | Deployed via DeployGuardians |
| PufferOracle                  | - | [0xD211960A914c8bCadFAf1Dff2d266127cbec55Bb](https://hoodi.etherscan.io/address/0xD211960A914c8bCadFAf1Dff2d266127cbec55Bb) | Deployed via DeployPufferOracle |
| PufferProtocol                | - | [0x182FcF340d50dEB1FCa0B15F9097025fC99DDB7c](https://hoodi.etherscan.io/address/0x182FcF340d50dEB1FCa0B15F9097025fC99DDB7c) | Deployed implementation |
| ValidatorTicket               | - | [0x6E0225679209459a355297A43B61cAFbC1Ca8d46](https://hoodi.etherscan.io/address/0x6E0225679209459a355297A43B61cAFbC1Ca8d46) | Deployed via DeployVTImplementation |
| PufferRevenueDepositor        | [0x028f33E487669A8Eed8934ad222CFCE7780FC32F](https://hoodi.etherscan.io/address/0x028f33E487669A8Eed8934ad222CFCE7780FC32F) | [0x5b85Ccd1a3DaF8fF993a3BF0ed0154Ebb09D7427](https://hoodi.etherscan.io/address/0x5b85Ccd1a3DaF8fF993a3BF0ed0154Ebb09D7427) | Deployed via DeployRevenueDepositor |
| PufferModule                  | - | [0x3E48EDF8c4b7229436e523938ffe9C5b724Ae7bf](https://hoodi.etherscan.io/address/0x3E48EDF8c4b7229436e523938ffe9C5b724Ae7bf) | Implementation only |
| RestakingOperator             | - | [0x2880A3D1819cbE51cdFBFf36d654b0E73c8a0e94](https://hoodi.etherscan.io/address/0x2880A3D1819cbE51cdFBFf36d654b0E73c8a0e94) | Implementation only |
| PufferModuleBeacon            | - | [0x34A2525D7ACE0C579B763FF15f59aE469A9Ab937](https://hoodi.etherscan.io/address/0x34A2525D7ACE0C579B763FF15f59aE469A9Ab937) | Beacon for PufferModule |
| RestakingOperatorBeacon       | - | [0x649ADE3a5cbAb61b9297Def8Ad19E2f04528222d](https://hoodi.etherscan.io/address/0x649ADE3a5cbAb61b9297Def8Ad19E2f04528222d) | Beacon for RestakingOperator |
| AVSContractsRegistry          | - | [0xcfc84cED34265A021C2652292dDe48c64A716e47](https://hoodi.etherscan.io/address/0xcfc84cED34265A021C2652292dDe48c64A716e47) | Registry for AVS contracts |
| RestakingOperatorController   | - | [0x7aD345dC8583015f31E8f03CAE9cA09706514349](https://hoodi.etherscan.io/address/0x7aD345dC8583015f31E8f03CAE9cA09706514349) | Controller for RestakingOperators |
| PufferModuleManager           | - | [0xD591b120c63916B1d195d54d863cff5d6632219e](https://hoodi.etherscan.io/address/0xD591b120c63916B1d195d54d863cff5d6632219e) | Module manager |

## External Contract Addresses (Used in Deployment)

| Name                          | Address | Source |
| ----------------------------- | ------- | ------ |
| stETH                         | [0xa1E64F52b83C9d0c2b2b5B7e16C8D5B9b3d8e4eA](https://hoodi.etherscan.io/address/0xa1E64F52b83C9d0c2b2b5B7e16C8D5B9b3d8e4eA) | Standard stETH on Hoodi testnet |
| WETH                          | [0x5c3D79EB9d343ed6b69D49Db1F7a000869886c6c](https://hoodi.etherscan.io/address/0x5c3D79EB9d343ed6b69D49Db1F7a000869886c6c) | Deployed via DeployPufETH |
| BeaconDepositContract         | [0x00000000219ab540356cBB839Cbe05303d7705Fa](https://hoodi.etherscan.io/address/0x00000000219ab540356cBB839Cbe05303d7705Fa) | Standard Ethereum Beacon Deposit Contract |

## EigenLayer Contracts on Hoodi

| Name                          | Address | Source |
| ----------------------------- | ------- | ------ |
| DelegationManager             | [0x867837a9722C512e0862d8c2E15b8bE220E8b87d](https://hoodi.etherscan.io/address/0x867837a9722C512e0862d8c2E15b8bE220E8b87d) | EigenLayer deployment |
| EigenPodManager               | [0xcd1442415Fc5C29Aa848A49d2e232720BE07976c](https://hoodi.etherscan.io/address/0xcd1442415Fc5C29Aa848A49d2e232720BE07976c) | EigenLayer deployment |
| StrategyManager               | [0xeE45e76ddbEDdA2918b8C7E3035cd37Eab3b5D41](https://hoodi.etherscan.io/address/0xeE45e76ddbEDdA2918b8C7E3035cd37Eab3b5D41) | EigenLayer deployment |
| AVSDirectory                  | [0xD58f6844f79eB1fbd9f7091d05f7cb30d3363926](https://hoodi.etherscan.io/address/0xD58f6844f79eB1fbd9f7091d05f7cb30d3363926) | EigenLayer deployment |
| AllocationManager             | [0x95a7431400F362F3647a69535C5666cA0133CAA0](https://hoodi.etherscan.io/address/0x95a7431400F362F3647a69535C5666cA0133CAA0) | EigenLayer deployment |
| RewardsCoordinator            | [0x29e8572678e0c272350aa0b4B8f304E47EBcd5e7](https://hoodi.etherscan.io/address/0x29e8572678e0c272350aa0b4B8f304E47EBcd5e7) | EigenLayer deployment |
| PermissionController          | [0xdcCF401fD121d8C542E96BC1d0078884422aFAD2](https://hoodi.etherscan.io/address/0xdcCF401fD121d8C542E96BC1d0078884422aFAD2) | EigenLayer deployment |
