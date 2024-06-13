# Repositories + CI/CD

## CI / CD

- **Version Control**
    - Found problem with code, can get back to an older version that worked

- **Agile**
    - Divide in small parts, then implement

- **Pipeline**
    - Workflow of code delivery process

## Test

- **Unit test**
    - Sandbox or dry run tests of individual components / configurations
    - Some networking equipment has this option

- **System test**
    - Deploy the different network components and test their interactions
    - Testing environment? Network emulator, virtualization

- **Staging environment**
    - Replica of production environment
    - Test specifics of production environment (number of nodes, addresses, etc.)

## Release vs deploy

- A **release** is the software product, ready to be deployed
- A **deployment** is a release configured for the target environment

- For **infrastructure**, a **release** includes the general setup configurations, whereas a **deployment** adapts those configurations to the particular infrastructure's characteristics and requirements.

## Abstractions and examples

- NETCONF communication with devices
- Ansible with NETCONF module for automation
- Github as repository
- Jenkins for automating CI/CD

- **Operations:**
    - **Build:** gets facts from deployment, validates configurations
    - **Test:** dry run in target devices (JunOS, commit-check)
    - **Deploy:** see if there are changes pending (config vs state of devices), only deploy changes