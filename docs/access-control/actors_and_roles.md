# Actors and Roles

## Actors

| Role                           	| Role ID 	| Actors                                             	| Requirement           	| Remarks                                                                                                    |
| :-----------------------------:	| :-------:	| :--------------------------------------------------	| :---------------------	| :--------------------------------------------------------------------------------------------------------- |
| ADMIN_ROLE                     	| 0       	| Timelock.sol                                       	|                       	|                                                                                                            |
| ROLE_ID_UPGRADER               	| 1       	| Community Multisig & Ops Multisig (7 days delay) 	    |                       	|                                                                                                            |
| ROLE_ID_AVS_COORDINATOR_ALLOWLISTER   	| 5      	| DAO                                          	|                  	| This role whitelists which AVSs the RestakingOperator contracts can opt in to.                            |
| ROLE_ID_OPERATIONS_PAYMASTER   	| 23      	| Paymaster                                          	| - EOA                 	| This role covers the gas costs but should not be relied on as the sole defense.                            |
| ROLE_ID_OPERATIONS_COORDINATOR 	| 24      	| Access Controlled smart contract with sanity checks  	|                        	| This role is for calling VT setMintPrice on Oracle                                                         |
| ROLE_ID_PUFFER_PROTOCOL        	| 1234    	| PufferProtocol.sol                                 	|                       	| This role is to restrict function calls so that only the PufferProtocol functions can call them            |
| ROLE_ID_DAO                    	| 77      	| Ops multisig until we have governance              	|                       	|                                                                                                            |
| ROLE_ID_OPERATIONS_MULTISIG    	| 22      	| Ops multisig                                       	|                       	|                                                                                                            |
| ROLE_ID_GUARDIANS              	| 88      	| — unused rn                                        	|                       	|                                                                                                            |
| PUBLIC_ROLE                    	| max_int 	| Public                                             	|                       	|                                                                                                            |


## Roles

| Role ID |           Full Title        |                    Description of the Role                                   |
| :-----: | :-------------------------: | :--------------------------------------------------------------------------- |
| 0       | ADMIN_ROLE                  | Administrative access for upgradability, only held by Timelock.              |
| 5       | ROLE_ID_AVS_COORDINATOR_ALLOWLISTER                | Whitelists AVSs that can be opted in to               |
| 7       | ROLE_ID_LOCKBOX             | xPufETH LockBox Contract.                                                    |
| 22      | ROLE_ID_OPERATIONS_MULTISIG | Operations multisig, manages operational tasks and transactions.             |
| 23      | ROLE_ID_OPERATIONS_PAYMASTER| Responsible for managing functional transactions and pay the operational gas.|
| 24      | ROLE_ID_OPERATIONS_COORDINATOR | Access Controlled smart contract with sanity checks for system variables. |
| 25      | ROLE_ID_VT_PRICER           | Role for the VT price poster.                                                |
| 77      | ROLE_ID_DAO                 | DAOs role which after formation will control the protocol                    |
| 1234    | ROLE_ID_PUFFER_PROTOCOL     | Main Puffer Protocol contract                                                |
| max_int | PUBLIC_ROLE                 | Public role for public functions                                             |   


