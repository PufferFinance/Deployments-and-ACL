# Contracts and Functions

## PufferModuleManager

|                 Function                	| Role ID |         Actor        |                  Remarks              |          Action Items        |
|:---------------------------------------:	|:-------:|:-------------------: |:------------------------------------- |:---------------------------  |
| createNewRestakingOperator              	| 77      | Ops Multisig         |                                       | Ops Multisig -> DAO          |
| callModifyOperatorDetails               	| 77      | Ops Multisig         |                                       | Ops Multisig -> DAO          |
| callOptIntoSlashing                     	| 77      | Ops Multisig         |                                       | Ops Multisig -> DAO          |
| callUpdateMetadataURI                   	| 77      | Ops Multisig         |                                       | Ops Multisig -> DAO          |
| callUndelegate                          	| 77      | Ops Multisig         |                                       | Ops Multisig -> DAO          |
| callDelegateTo                          	| 77      | Ops Multisig         |                                       | Ops Multisig -> DAO          |
| updateAVSRegistrationSignatureProof     	| 77      | Ops Multisig         |                                       | Ops Multisig -> DAO          |
| callRegisterOperatorToAVS               	| 77      | Ops Multisig         |                                       | Ops Multisig -> DAO          |
| callRegisterOperatorToAVSWithChurn      	| 77      | Ops Multisig         |                                       | Ops Multisig -> DAO          |
| callDeregisterOperatorFromAVS           	| 77      | Ops Multisig         |                                       | Ops Multisig -> DAO          |
| callUpdateOperatorAVSSocket             	| 77      | Ops Multisig         |                                       | Ops Multisig -> DAO          |
| callQueueWithdrawals                    	| 23      | Paymaster & Guardians|                                       |                              |
| callWithdrawNonBeaconChainETH BalanceWei 	| 23      | Paymaster            |                                       |                              |
| callVerifyAndProcessWithdrawals           | 23      | Paymaster & Guardians|                                     	 | Paymaster -> Public          |
| callCompleteQueuedWithdrawals             | 23      | Paymaster            |                                       |                              |
| callVerifyWithdrawalCredentials           | max_int | Public               |                                       |                              |
| UpgradeableBeacon.upgradeTo               | 0       | Timelock.sol         |                                       |                              |


## ValidatorTicket

|              Function                    	| Role ID |         Actor        |                           Remarks                      |          Action Items        |
|:---------------------------------------:	|:-------:|:-------------------: |:------------------------------------------------------ |:---------------------------  |
| setProtocolFeeRate                      	| 77      | Ops Multisig         |                                                        | Ops Multisig -> DAO          |
| setGuardiansFeeRate                     	| 77      | Ops Multisig         |                                                        | Ops Multisig -> DAO          |
| purchaseValidatorTicket                  	| max_int | Public               |                                                        |                             	|
| burn                                    	| max_int | Public               |                                                        |                             	|
| UUPSUpgradeable. upgradeToAndCall         | 0       | Timelock.sol         |                                                        |                         	    |


## GuardianModule

|                 Function                	| Role ID |         Actor        |                       Remarks                    |          Action Items        |
|:---------------------------------------:	|:-------:|:-------------------: |:------------------------------------------------ |:---------------------------  |
| setGuardianEnclaveMeasurements          	| 77      | Ops Multisig         |                                                  | Ops Multisig -> DAO          |
| addGuardian                             	| 77      | Ops Multisig         |                                                  | Ops Multisig -> DAO          |
| removeGuardian                          	| 77      | Ops Multisig         |                                                  | Ops Multisig -> DAO          |
| setEjectionThreshold                    	| 77      | Ops Multisig         |                                                  | Ops Multisig -> DAO          |
| setThreshold                            	| 77      | Ops Multisig         |                                                  | Ops Multisig -> DAO          |


## PufferProtocol

|                 Function                | Role ID |         Actor        |                     Remarks                      |          Action Items        |
| :------------------------------------:  |:-------:|:-------------------: |:------------------------------------------------ |:---------------------------  |
| createPufferModule                      | 77      | Ops Multisig         |                                                  | Ops Multisig -> DAO          |
| setModuleWeights                        | 77      | Ops Multisig         |                                                  | Ops Multisig -> DAO          |
| setValidatorLimitPerModule              | 77      | Ops Multisig         |                                                  | Ops Multisig -> DAO          |
| changeMinimumVTAmount                   | 77      | Ops Multisig         |                                                  | Ops Multisig -> DAO          |
| setVTPenalty                            | 77      | Ops Multisig         |                                                  | Ops Multisig -> DAO          |
| provisionNode                           | 23 	    | Paymaster & Guardians|                                                  |                              |
| skipProvisioning                        | 23 	    | Paymaster & Guardians|                                                  |                              |
| batchHandleWithdrawals                  | 23 	    | Paymaster & Guardians|                                                  |                              |
| registerValidatorKey                    | max_int | Public               |                                                  |                            	 |
| depositValidatorTickets                 | max_int | Public               |                                                  |                              |
| withdrawValidatorTickets                | max_int | Public               |                                                  |                              |
| revertIfPaused                          | max_int | Public               |                                                  |                              |
| UUPSUpgradeable. upgradeToAndCall       | 0       | Timelock.sol         |                                                  |                              |



## EnclaveVerifier

|                 Function                	| Role ID |         Actor        |                           Remarks                      |          Action Items        |
|:---------------------------------------:	|:-------:|:-------------------: |:------------------------------------------------------ |:---------------------------  |
| removeLeafX509                          	| 77      | Ops Multisig         | To be deprecated                                       |                              |


## PufferVault

|                 Function                | Role ID |         Actor        |                           Remarks                |          Action Items        |
|:---------------------------------------:|:-------:|:-------------------: |:------------------------------------------------ |:---------------------------  |
| setDailyWithdrawalLimit                 | 77      | Ops Multisig         |                                                  |                              |
| setExitFeeBasisPoints                   | 77      | Ops Multisig         |                                                  |                              |
| initiateETHWithdrawalsFromLido          | 22      | Ops Multisig         |                                                  |                              |
| claimWithdrawalsFromLido                | 22      | Ops Multisig         |                                                  |                              |
| claimWithdrawalFromEigenLayerM2         | 22      | Ops Multisig         |                                                  |                              |
| transferETH                             | 1234    | PufferProtocol       | Initiated from PufferProtocol. provisionNode()   |                              |
| burn                                    | 1234    | PufferProtocol       | Initiated from PufferProtocol. batchHandleWithdrawals() |                       |
| depositToEigenLayer                     | 22      | Ops Multisig         |                                                  |                              |
| initiateStETHWithdrawalFromEigenLayer   | 22  	| Ops Multisig         |                                                  |                              |
| PufferVault                             | max_int |  Public              |                                                  |                              |
| deposit                                 | max_int |  Public              |                                                  |                              |
| mint                                    | max_int |  Public              |                                                  |                              |
| withdraw                                | max_int |  Public              |                                                  |                              |
| redeem                                  | max_int |  Public              |                                                  |                              |
| depositStETH                            | max_int |  Public              |                                                  |                              |
| depositWstETH                           | max_int |  Public              |                                                  |                              |


## OperationsCoordinator

|                 Function                	| Role ID |         Actor        |                           Remarks                      |          Action Items        |
|:---------------------------------------:	|:-------:|:-------------------: |:------------------------------------------------------ |:---------------------------  |
| setValidatorTicketMintPrice              	| 23      | Paymaster            |                                                        |                              |
| setPriceChangeToleranceBps               	| 22      | Ops Multisig         |                                                        |                              |



## PufferDepositor

|                 Function                | Role ID |         Actor        |                           Remarks                |          Action Items        |
|:---------------------------------------:|:-------:|:-------------------: |:------------------------------------------------ |:---------------------------  |
| depositStETH                            | max_int |  Public              |                                                  |                              |
| depositWstETH                           | max_int |  Public              |                                                  |                              |


## PufferOracle

|                 Function                	| Role ID |         Actor        |                           Remarks                      |          Action Items        |
|:---------------------------------------:	|:-------:|:-------------------: |:------------------------------------------------------ |:---------------------------  |
| provisionNode                           	| 1234    | PufferProtocol       | Initiated from PufferProtocol. provisionNode()         |                              |
| exitValidators                          	| 1234    | PufferProtocol       | Initiated from PufferProtocol. batchHandleWithdrawals()|                              |
| setTotalNumberOfValidators              	| 22 	  | Ops Multisig         |                                                        |                              |
| setMintPrice                            	| 24      | Ops Coordinator      |                                                        |                              |

## AccessManager

|                 Function                	| Role ID |         Actor        |                     Remarks                      |          Action Items        |
|:---------------------------------------:	|:-------:|:-------------------: |:------------------------------------------------ |:---------------------------  |
| grantRole                                	| 77      | Ops Multisig         |Has 7 days delay                                  | Ops Multisig -> DAO          |
| grantRole                                 | 1234    | PufferProtocol       |                                                  |                              |
