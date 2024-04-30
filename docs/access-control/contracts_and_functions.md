# Contracts and Functions

## PufferModuleManager

|                 Function                	| Role ID |         Actor        |                                                  Address                                      	|                  Remarks                    |          Action Items        |
|:---------------------------------------:	|:-------:|:-------------------: |:----------------------------------------------------------------------------------------------:|:------------------------------------------- |:---------------------------  |
| createNewRestakingOperator              	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                             | Ops Multisig -> DAO          |
| callModifyOperatorDetails               	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                             | Ops Multisig -> DAO          |
| callOptIntoSlashing                     	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                             | Ops Multisig -> DAO          |
| callUpdateMetadataURI                   	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                             | Ops Multisig -> DAO          |
| callUndelegate                          	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                             | Ops Multisig -> DAO          |
| callDelegateTo                          	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                             | Ops Multisig -> DAO          |
| updateAVSRegistrationSignatureProof     	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                             | Ops Multisig -> DAO          |
| callRegisterOperatorToAVS               	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                             | Ops Multisig -> DAO          |
| callRegisterOperatorToAVSWithChurn      	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                             | Ops Multisig -> DAO          |
| callDeregisterOperatorFromAVS           	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                             | Ops Multisig -> DAO          |
| callUpdateOperatorAVSSocket             	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                             | Ops Multisig -> DAO          |
| callQueueWithdrawals                    	| 23      | Paymaster & Guardians| [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                             | Ops Multisig -> Paymaster    |
| callWithdrawNonBeaconChainETH BalanceWei 	| 23      | Paymaster            | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                             | Ops Multisig -> Paymaster    |
| callVerifyAndProcessWithdrawals           | 23      | Paymaster & Guardians| [0x3C28B7c...f2126eA](https://etherscan.io/address/0x3C28B7c7Ba1A1f55c9Ce66b263B33B204f2126eA) |                                           	| Paymaster -> Public          |
| callCompleteQueuedWithdrawals             | 23      | Paymaster            |                                                                                                |                                             |                              |
| callVerifyWithdrawalCredentials           | max_int | Public               |                                                                                                |                                           	|                              |
| UpgradeableBeacon.upgradeTo               | 0       | Timelock.sol         | [0x3C28B7c...f2126eA](https://etherscan.io/address/0x3C28B7c7Ba1A1f55c9Ce66b263B33B204f2126eA) |                                             |                              |


## ValidatorTicket

|              Function                    	| Role ID |         Actor        |                                                  Address                                        	|                           Remarks                      |          Action Items        |
|:---------------------------------------:	|:-------:|:-------------------: |:----------------------------------------------------------------------------------------------:	|:------------------------------------------------------ |:---------------------------  |
| setProtocolFeeRate                      	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) 	|                                                        | Ops Multisig -> DAO          |
| setGuardiansFeeRate                     	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) 	|                                                        | Ops Multisig -> DAO          |
| purchaseValidatorTicket                  	| max_int | Public               |                                                                                                	|                                                        |                             	|
| burn                                    	| max_int | Public               |                                                                                                	|                                                        |                             	|
| UUPSUpgradeable. upgradeToAndCall         	| 0       | Timelock.sol         | [0x3C28B7c...f2126eA](https://etherscan.io/address/0x3C28B7c7Ba1A1f55c9Ce66b263B33B204f2126eA) 	|                                                        |                         	    |


## GuardianModule

|                 Function                	| Role ID |         Actor        |                                                  Address                                       	|                           Remarks                      |          Action Items        |
|:---------------------------------------:	|:-------:|:-------------------: |:----------------------------------------------------------------------------------------------:	|:------------------------------------------------------ |:---------------------------  |
| setGuardianEnclaveMeasurements          	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) 	|                                                        | Ops Multisig -> DAO          |
| addGuardian                             	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) 	|                                                        | Ops Multisig -> DAO          |
| removeGuardian                          	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) 	|                                                        | Ops Multisig -> DAO          |
| setEjectionThreshold                    	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) 	|                                                        | Ops Multisig -> DAO          |
| setThreshold                            	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) 	|                                                        | Ops Multisig -> DAO          |


## PufferProtocol

|                 Function                | Role ID |         Actor        |                                                  Address                                       	|                           Remarks                      |          Action Items        |
| :------------------------------------:  |:-------:|:-------------------: |:----------------------------------------------------------------------------------------------:	|:------------------------------------------------------ |:---------------------------  |
| createPufferModule                      | 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) 	|                                                        | Ops Multisig -> DAO          |
| setModuleWeights                        | 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) 	|                                                        | Ops Multisig -> DAO          |
| setValidatorLimitPerModule              | 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) 	|                                                        | Ops Multisig -> DAO          |
| changeMinimumVTAmount                   | 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) 	|                                                        | Ops Multisig -> DAO          |
| setVTPenalty                            | 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) 	|                                                        | Ops Multisig -> DAO          |
| provisionNode                           | 23 	    | Paymaster & Guardians|                                                                                                	|                                                        |                              |
| skipProvisioning                        | 23 	    | Paymaster & Guardians|                                                                                                	|                                                        |                              |
| batchHandleWithdrawals                  | 23 	    | Paymaster & Guardians|                                                                                                	|                                                        |                              |
| registerValidatorKey                    | max_int | Public               |                                                                                                	|                                                        |                            	|
| depositValidatorTickets                 | max_int | Public               |                                                                                                	|                                                        |                             	|
| withdrawValidatorTickets                | max_int | Public               |                                                                                                	|                                                        |                             	|
| revertIfPaused                          | max_int | Public               |                                                                                                	|                                                        |                             	|
| UUPSUpgradeable. upgradeToAndCall       | 0       | Timelock.sol         | [0x3C28B7c...f2126eA](https://etherscan.io/address/0x3C28B7c7Ba1A1f55c9Ce66b263B33B204f2126eA) 	|                                                        |                              |



## EnclaveVerifier

|                 Function                	| Role ID |         Actor        |                                                  Address                                        	|                           Remarks                      |          Action Items        |
|:---------------------------------------:	|:-------:|:-------------------: |:----------------------------------------------------------------------------------------------:	|:------------------------------------------------------ |:---------------------------  |
| removeLeafX509                          	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) 	| To be deprecated                                       |                              |


## PufferVault

|                 Function                | Role ID |         Actor        |                                                  Address                                       |                           Remarks                |          Action Items        |
|:---------------------------------------:|:-------:|:-------------------: |:----------------------------------------------------------------------------------------------:|:------------------------------------------------ |:---------------------------  |
| setDailyWithdrawalLimit                 | 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                                  |                              |
| setExitFeeBasisPoints                   | 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                                  |                              |
| initiateETHWithdrawalsFromLido          | 22      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                                  |                              |
| claimWithdrawalsFromLido                | 22      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                                  |                              |
| claimWithdrawalFromEigenLayerM2         | 22      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) |                                                  |                              |
| transferETH                             | 1234    | PufferProtocol       | [0x716B75d...e84604E](https://etherscan.io/address/0x716B75d22B5e5f5cCa2C7229F6df79DEEe84604E) | Initiated from PufferProtocol. provisionNode()   |                              |
| burn                                    | 1234    | PufferProtocol       | [0x716B75d...e84604E](https://etherscan.io/address/0x716B75d22B5e5f5cCa2C7229F6df79DEEe84604E) | Initiated from PufferProtocol. batchHandleWithdrawals() |                       |
| depositToEigenLayer                     | 22      | Ops Multisig         | [0x3C28B7c...f2126eA](https://etherscan.io/address/0x3C28B7c7Ba1A1f55c9Ce66b263B33B204f2126eA) |                                                  |                              |
| initiateStETHWithdrawalFromEigenLayer   | 22  	| Ops Multisig         | [0x3C28B7c...f2126eA](https://etherscan.io/address/0x3C28B7c7Ba1A1f55c9Ce66b263B33B204f2126eA) |                                                  |                              |
| PufferVault                             | max_int |  Public              |                                                                                                |                                                  |                              |
| deposit                                 | max_int |  Public              |                                                                                                |                                                  |                              |
| mint                                    | max_int |  Public              |                                                                                                |                                                  |                              |
| withdraw                                | max_int |  Public              |                                                                                                |                                                  |                              |
| burn                                    | max_int |  Public              |                                                                                                |                                                  |                              |
| redeem                                  | max_int |  Public              |                                                                                                |                                                  |                              |
| depositStETH                            | max_int |  Public              |                                                                                                |                                                  |                              |
| depositWstETH                           | max_int |  Public              |                                                                                                |                                                  |                              |


## PufferDepositor

|                 Function                | Role ID |         Actor        |                                                  Address                                       |                           Remarks                |          Action Items        |
|:---------------------------------------:|:-------:|:-------------------: |:----------------------------------------------------------------------------------------------:|:------------------------------------------------ |:---------------------------  |
| depositStETH                            | max_int |  Public              |                                                                                                |                                                  |                              |
| depositWstETH                           | max_int |  Public              |                                                                                                |                                                  |                              |
| swapAndDeposit                          | max_int |  Public              |                                                                                                | Paused - Deprecated                              |                              |
| swapAndDepositWithPermit                | max_int |  Public              |                                                                                                | Paused - Deprecated                              |                              |
| swapAndDepositWithPermit1Inch           | max_int |  Public              |                                                                                                | Paused - Deprecated                              |                              |
| swapAndDeposit1Inch                     | max_int |  Public              |                                                                                                | Paused - Deprecated                              |                              |


## PufferOracle

|                 Function                	| Role ID |         Actor        |                                                  Address                                       	|                           Remarks                      |          Action Items        |
|:---------------------------------------:	|:-------:|:-------------------: |:----------------------------------------------------------------------------------------------:	|:------------------------------------------------------ |:---------------------------  |
| provisionNode                           	| 1234    | PufferProtocol       | [0x716B75d...e84604E](https://etherscan.io/address/0x716B75d22B5e5f5cCa2C7229F6df79DEEe84604E) 	| Initiated from PufferProtocol. provisionNode()         |                              |
| exitValidators                          	| 1234    | PufferProtocol       | [0x716B75d...e84604E](https://etherscan.io/address/0x716B75d22B5e5f5cCa2C7229F6df79DEEe84604E) 	| Initiated from PufferProtocol. batchHandleWithdrawals()|                              |
| setTotalNumberOfValidators              	| 22 	  | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) 	|                                                        |                              |
| setMintPrice                            	| 24      | Ops Coordinator      |   |   |

## AccessManager

|                 Function                	| Role ID |         Actor        |                                                  Address                                       	|                           Remarks                      |          Action Items        |
|:---------------------------------------:	|:-------:|:-------------------: |:----------------------------------------------------------------------------------------------:	|:------------------------------------------------------ |:---------------------------  |
| grantRole                                	| 77      | Ops Multisig         | [0xC0896ab...955580d](https://etherscan.io/address/0xC0896ab1A8cae8c2C1d27d011eb955Cca955580d) 	|  Has 7 days delay                                      | Ops Multisig -> DAO          |
| grantRole                                 | 1234    | PufferProtocol       | [0x716B75d...e84604E](https://etherscan.io/address/0x716B75d22B5e5f5cCa2C7229F6df79DEEe84604E) 	|                                                        |                              |
