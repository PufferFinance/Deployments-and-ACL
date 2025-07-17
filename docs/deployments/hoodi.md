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
| RestakingOperator             | - | [0x67b40a2335dd1c620B23ab5EDF4F32C767E43920](https://hoodi.etherscan.io/address/0x67b40a2335dd1c620B23ab5EDF4F32C767E43920) | Implementation only |
| PufferModuleBeacon            | - | [0x34A2525D7ACE0C579B763FF15f59aE469A9Ab937](https://hoodi.etherscan.io/address/0x34A2525D7ACE0C579B763FF15f59aE469A9Ab937) | Beacon for PufferModule |
| RestakingOperatorBeacon       | - | [0xf753Fbe66869E24be90eE726e1D02709fa46D775](https://hoodi.etherscan.io/address/0xf753Fbe66869E24be90eE726e1D02709fa46D775) | Beacon for RestakingOperator |
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
| DelegationManager             | [0x1b7b8F6b258f95Cf9596EabB9aa18B62940Eb0a8](https://hoodi.etherscan.io/address/0x1b7b8F6b258f95Cf9596EabB9aa18B62940Eb0a8) | EigenLayer deployment |
| EigenPodManager               | [0x30770d7E3e71112d7A6b7259542D1f680a70e315](https://hoodi.etherscan.io/address/0x30770d7E3e71112d7A6b7259542D1f680a70e315) | EigenLayer deployment |
| AllocationManager             | [0x95a7431400F362F3647a69535C5666cA0133CAA0](https://hoodi.etherscan.io/address/0x95a7431400F362F3647a69535C5666cA0133CAA0) | EigenLayer deployment |
| RewardsCoordinator            | [0x29e8572678e0c272350aa0b4B8f304E47EBcd5e7](https://hoodi.etherscan.io/address/0x29e8572678e0c272350aa0b4B8f304E47EBcd5e7) | EigenLayer deployment |

## Deployment Summary

1. **PufETH + AccessManager** - `0xd4A57B33bB84903e7B180f885bb64a2a8b140D85`
   - Includes stETH, WETH, and AccessManager deployment
   - AccessManager: `0x74Cec4ACf425458c9FD1c792Ed2DE6e2339F7b59`

2. **GuardianModule** - `0x711d5f6c1fa2E6dC11eD60Aa420647c8156DFd73`
   - Deployed with guardian address configuration

3. **PufferOracle** - `0xD211960A914c8bCadFAf1Dff2d266127cbec55Bb`
   - Deployed with AccessManager, GuardianModule, and PufferVault

4. **PufferProtocol** - `0x182FcF340d50dEB1FCa0B15F9097025fC99DDB7c`
   - Implementation deployed and verified

5. **ValidatorTicket** - `0x6E0225679209459a355297A43B61cAFbC1Ca8d46`
   - Deployed with treasury and operations multisig placeholders

6. **PufferRevenueDepositor** - `0x028f33E487669A8Eed8934ad222CFCE7780FC32F`
   - Proxy deployed with implementation at `0x5b85Ccd1a3DaF8fF993a3BF0ed0154Ebb09D7427`

7. **PufferModule Implementation** - `0x3E48EDF8c4b7229436e523938ffe9C5b724Ae7bf`
   - Implementation deployed and verified

8. **RestakingOperator Implementation** - `0x67b40a2335dd1c620B23ab5EDF4F32C767E43920`
   - Implementation deployed and verified with EigenLayer contracts

9. **PufferModuleBeacon** - `0x34A2525D7ACE0C579B763FF15f59aE469A9Ab937`
   - Beacon deployed pointing to PufferModule implementation

10. **RestakingOperatorBeacon** - `0xf753Fbe66869E24be90eE726e1D02709fa46D775`
    - Beacon deployed pointing to RestakingOperator implementation

11. **AVSContractsRegistry** - `0xcfc84cED34265A021C2652292dDe48c64A716e47`
    - Registry for AVS contracts deployed

12. **RestakingOperatorController** - `0x7aD345dC8583015f31E8f03CAE9cA09706514349`
    - Controller for RestakingOperators deployed

13. **PufferModuleManager** - `0xD591b120c63916B1d195d54d863cff5d6632219e`
    - Module manager deployed with all required beacon dependencies
