# Puffer Protocol Deployments & Access-Control List

This document provides lists of the latest deployments of the Puffer Protocol contracts, as well as, the access control list for the protocol. Additionally, this repository (including Github issues, PRs, actions) is the primary source of truth for the protocol, which provides a built-in change log and audit trail.

## Table of Contents

- [Deployment Records](docs/deployments/) - Deployment details for various networks.
  - [Mainnet](docs/deployments/mainnet.md)
  - [Holesky](docs/deployments/holesky.md)
  - [Scroll](docs/deployments/scroll.md)

- [ABIs](docs/abis/) - ABIs of deployed smart contracts
  - [PufferVault](docs/abis/PufferVault.json)
  - [PufferDepositor](docs/abis/PufferDepositor.json)
  - [PufferProtocol](docs/abis/PufferProtocol.json)
  - [OperationsCoordinator](docs/abis/OperationsCoordinator.json)
  - [GuardianModule](docs/abis/GuardianModule.json)
  - [PufferModuleManager](docs/abis/PufferModuleManager.json)
  - [PufferModule](docs/abis/PufferModule.json)
  - [PufferOracle](docs/abis/PufferOracle.json)
  - [RestakingOperator](docs/abis/RestakingOperator.json)
  - [ValidatorTicket](docs/abis/ValidatorTicket.json)
  - [EnclaveVerifier](docs/abis/EnclaveVerifier.json)
  - [Timelock](docs/abis/Timelock.json)


- [Access Control](docs/access-control/) - Access control details for various contracts.
  - [Actors and Roles](docs/access-control/actors_and_roles.md) - Description of roles and permissions within the system.
  - [Contracts and Functions](docs/access-control/contracts_and_functions.md) - Description of contracts, functions and their associated roles within the system.
  - [Function Selectors](docs/access-control/functionSelectors.md) - List of function selectors/signatures in the contracts.


- [logs](logs/) - Logs of various activities and transactions.
  - [Transaction Reports](logs/transactions.md) - Automated reports of transactions fetched and formatted.

- [Important Notes](docs/important_notes.md) - Critical information and other important notes regarding the change management.
