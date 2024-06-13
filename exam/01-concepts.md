# Concept Overview Sprint

## Management vs Operations

-   **Management:**
    - Network management is the process of administering and managing computer networks. Services provided by this discipline include fault analysis, performance management, provisioning of networks and maintaining quality of service. Network management software is used by network administrators to help perform these functions. 

    -   Conceptual, high-level dimensions to keep network running smoothly;
    -   **smoothly:** QoE (Quality of Experience), reliability, security, etc.
    -   manage monitoring, configurations, performance, faults, security, accounting, etc.

-   **Operations**
    -   people, processes, and tools to make management happen;
    -   typically in the network operation center.

## Control Plane and Data Plane

**Data Plane:** In contrast to the control plane, which determines how packets should be forwarded, the data plane actually forwards the packets. The data plane is also called the forwarding plane.

Think of the control plane as being like the stoplights that operate at the intersections of a city. Meanwhile, the data plane (or the forwarding plane) is more like the cars that drive on the roads, stop at the intersections, and obey the stoplights.

Some examples of data planes include: - Ethernet networks - Wi-Fi networks - Cellular networks - Satellite communications

**Control Plane**: The control plane is the part of a network that controls how data packets are forwarded — meaning how data is sent from one place to another. The process of creating a routing table, for example, is considered part of the control plane. Routers use various protocols to identify network paths, and they store these paths in routing tables.

Control Plane uses various protocols, such as: - Routing protocols (BGP, OSPF, IS-IS, ...) - Network management protocols (SNMP) - Application layer protocols (HTTP and FTP)

#### Differences

The control plane decides how data is managed, routed, and processed, while the data plane is responsible for the actual moving of data. For example, the control plane decides how packets should be routed, and the data plane carries out those instructions by forwarding the packets.

| Control Plane                                               | Data Plane                                                |
| ----------------------------------------------------------- | --------------------------------------------------------- |
| Determines how data should be managed, routed and processed | Responsible for moving packets from source to destination |
| Builds and maintains the IP routing table | Forwards actual IP packets based on the Control Plane's logic |
| Packets are processed by the router to update the routing table | Forwards packets based on the built logic of the Control Plane |


## DevOps

### In the cloud

- **Traditional release deployment:**
    - Gather specs, UML architecture diagrams, implement, test, deploy
    - silos: dev team => |fence| => ops team
    - dev does not consider operational requirements
    - broken deployments, long feedback to dev

- **Devops approach:**
    - quick deployment cycle (agile, test-driven, sprints)
    - write code thinking about other phases (deployment, testing, etc.)
    - build rather than buy
    - automate test and deployment - repeatable, predictable
    - embrace failure (aka fail fast, find errors/vulnerabilities and recover quickly)

### For networking

 - Harder
    - More physical limitations - cables, device access
    - Hard to control - heterogeneous device APIs
    - Complex - multiple protocols, topologies, etc.
    - Hardware bundle - switching, routing, etc. in same closed box

- If we can do this, then we have:
    - **Quick deployment** - provisioning, updates, new devices, disaster recovery
    - **Predictable deployment** - same code, same outputs - no typos or missing commands in the console
    - **Fail fast** - quick rollback to previous configuration or quickly fix errors and redeploy
    - **Build rather than buy** - and even when buying, automating the 20% of the tasks that we need but that the device does not automate

##### Moving towards devops

- **Virtual Networks**
    - Connect remote devices as if in the same L2/L3 network - vxlan, etc.

- **Software Defined Networks**
    - Well defined, open interface to upload switching rules
    - Flexible creation of networks, paths, etc across different devices
    - Many use SDN but don't actually need it - could use vlan and friends

- **Network Function Virtualization**
    - Enables running network functions (routing, etc) in generic hardware
    - Network functions in containers or VMs - quick, predictable deployment
    - x86-like devices popping up in the network, VMs connected by virtual switches

- **Programmatic device interfaces**
    - Richer interfaces for interacting programmatically with devices

- **Anyone can write code**

## FCAPS

FCAPS stands for:

**F**ault
**C**onfiguration
**A**ccounting
**P**erformance
**S**ecurity

FCAPS is a network management framework created by the International Organization for Standardization (ISO). The primary objective of this network management model is to better understand the major functions of network management systems. Its goal was to move away from a reactive form of network management to a proactive approach -- for example, to empower administrators to take more control of their infrastructure to identify an rectify minor issues before they become major problems.

### Fault Management 

A fault is an event that has a lot of significance, The goal of fault management is to recognize, isolate, correct and log faults that occur in the network. Furthemore, it uses trend analysis to predict errors so that the network is always available. This can be established by monitoring different things for abnormal behaviour.

When a fault or event occurs, a network component will often send a notification to the network operator using either a proprietary protocol such as SNMP, to collect information about network devices or at least write a message to its console for a console server to catch and log/page. In turn, the management station can be configured to make a network administrator aware of problems, allowing appropriate actions to be taken. This notification is supposed to trigger manual or automatic activities. For example, the gathering of more data to identify the nature and severity of the problem to bring backup equipment on-line. 

Fault logs are one input used to compile statistics to determine the provided service level of individual network elements, as well as sub-networks or the whole network. They are also used to determine apparently fragile network components that require further attention. Errors primarily occur in the areas of fault management and configuration management.

Network elements produce alarms (also known as traps or indications) that are monitored by a Fault management system. This function is known as alarm surveillance.

### Configuration Management

The goals of configuration management include:

- to gather and store configurations from network devices (this can be done locally or remotely).
- to simplify the configuration of the device
- to track changes that are made to the configuration
- to configure ('provision') circuits or paths through non-switched networks
- to plan for future expansion and scaling

Configuration management is concerned with monitoring system configuration information, and any changes that take place. This are is especially important, since many network issues arise as a direct result of changes made to configuration files, updated software versions, or changes to the system hardware. A proper configuration management strategy involves tracking all changes made to network hardware and software. Examples include altering the running configuration of a device, updating the OS version of a router or switch, or adding a new modular interface card. A good approach instead of doing this manually is to use configuration management software.

### Accounting Management

The goal is to gather usage statistics for users.

Accounting management is concerned with tracking network utilization information, such that individual users, departments, or business units can be appropriately billed or charged for accounting purposes. While this may not be applicable to all companies, in many large orgs, the IT department is considered a cost center that accrues revenues according to resource utilization by individual departments or business units. For non-billed networks, "administration" replaces "accounting". The goals of administration are to administer the set of authorized users by establishing users, passwords and permissions, and to administer the operations of the equipment such as by performing software backup and synchronization.

Accounting is often referred to as billing management. Using the statistic, the users can be billed and usage quotas can be enforced. These can be disk usage, link utilization, CPU time, etc.

### Performance Management

Performance management is focused on ensuring that network performance remains at acceptable levels. It enables the manager to prepare the network for the future, as well as to determine the efficient of the current network, for example, in relation to the investments done to set it up. The network performance addresses the throughput, network response times, packet loss rates, link utilization, percentage utilization, error rates, and so foth.

This information is usually gathered through the implementation of an SNMP management system, either actively monitored, or configured to alert administrators when performance moves above or below predefined thresholds. Actively monitoring current network performance is an important step in identifying problems before they occur, as part of a proactive network management strategy. By collecting ana analysing performance data, the network health can be monitored. Trends can indicate capacity or reliability issues before they affect services. Also, performance thresholds can be set in order to trigger an alarm. 

### Security Management

Security management is the process of controlling access to assets in the network. Data security can be achieved mainly with authentication and encryption. Authorization to it configured with OS and DBMS access control setting.

Security management is not only concerned with ensuring that a network environment is secure, but also that gathered security-related information is analyzed regularly. Security management functions include managing network authentication, authorization, and auditing, such that both internal and external users only have access to appropriate network resources. Other common tasks include the configuration and management of network firewalls, intrusion detection systems, and security policies (such as access lists). Network elements keep log files, which are examined during a security audit.

## SNMP 
Simple Network Management Protocol (SNMP) is an Internet Standard protocol for collecting and organizing information about managed devices on IP networks and for modifying that information to change device behavior. Devices that typically support SNMP include cable modems, routers, switches, servers, workstations, printers, and more.

SNMP is widely used in network management for network monitoring. SNMP exposes management data in the form of variables on the managed systems organized in a management information base (MIB), which describes the system status and configuration. These variables can then be remotely queried (and, in some circumstances, manipulated) by managing applications. 


