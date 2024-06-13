# Exam - Network and Systems Management (M.EIC017)

## Section A

### 1. Which of the following IP addresses is a private IP address? (Select all that apply)

-   a) 12.0.0.1
-   b) 168.182.19.39
-   c) 172.40.14.36
-   **d) 172.31.194.30**
-   **e) 10.0.255.4**

### 2. What protocol allows multiple hosts to dynamically obtain IP addresses from a server?

-   a) DNS
-   **b) DHCP**
-   c) WINS
-   d) ARP
-   e) ICMP

### 3. What is the range of assignable IP addresses for a subnet containing an IP address of 172.16.1.10 /19?

-   a) **172.16.0.1 – 172.16.31.254**
-   b) 172.16.0.1 – 172.16.63.254
-   c) 172.16.0.0 – 172.16.31.255
-   d) 172.16.0.1 – 172.16.31.255
-   e) 172.16.0.0 – 172.16.63.254

### 4. You assign IP addresses to hosts in the 192.168.4.0 /26 subnet. Which two of the following IP addresses are assignable IP addresses that reside in that subnet?

-   a) 192.168.4.0
-   b) 192.168.4.63
-   **c) 192.168.4.62**
-   **d) 192.168.4.32**
-   e) 192.168.4.64

### 5. A host in your network has been assigned an IP address of 192.168.181.182 /25. What is the subnet to which the host belongs?

-   **a) 192.168.181.128 /25**
-   b) 192.168.181.0 /25
-   c) 192.168.181.176 /25
-   d) 192.168.181.192 /25
-   e) 192.168.181.160 /25

### 6. In the network shown below, what is the most efficient summarization/aggregation that Router in Winnipeg can use to advertise its networks to Router in Vancouver?

![question 6](../../assets/meic017-p6.png)

-   a) 172.16.64.0/22 172.16.66.0/22
-   b) 172.16.32.0/22
-   c) 172.16.64.0/24 172.16.65.0/24 172.16.66.0/24 172.16.67.0/24
-   d) **172.16.64.0/22**
-   e) 172.16.64.0/21

### 7. Router is running BGP. What kind of packets does BGP send on this router to keep up connectivity with its neighbouring routers?

-   a) SPF packets
-   b) Hello packets
-   c) **Keepalive packets**
-   d) Dead interval packets
-   e) LSU packets

### 8. Which of the following are true statements regarding the characteristics of the OSPF areas? Select all that apply.

-   a) All OSPF networks require the use of multiple areas
-   b) **Multiple OSPF areas must connect to area 0.**
-   c) Single-area OSPF networks must be configured in area 1.
-   d) Areas may be assigned any number from 0 to 65535.
-   e) **Area 0 is called the backbone area.**
-   f) Each OSPF area requires a loopback interface to be configured.

### 9. Which aspect of network management does the "C" in FCAPS represent?

-   a) **Configuration Management**
-   b) Connection Management
-   c) Capacity Management
-   d) Compliance Management

### 10. What is DiffServ's (Differentiated Services) purpose in network management?

-   a) To ensure end-to-end encryption of network traffic
-   **b) To provide Quality of Service (QoS) for different types of network traffic**
-   c) To establish secure VPN connections between network devices
-   d) To monitor and manage network performance using SNMP

### 11. Which statement accurately describes the role of Root Authoritative Servers in the DNS (Domain Name System) hierarchy?

- a) They are responsible for resolving all internet users' domain names to IP addresses.
- b) They store and manage the DNS records for specific domains, such as "example.com".
- **c) They maintain the top-level domain (TLD) zone files, such as ".com", ".org", or ".net".**
- d) They cache frequently accessed DNS records to improve the performance of DNS lookups

### 12. Which statement accurately describes the role of BGP (Border Gateway Protocol) in network routing?

- a) BGP is a distance-vector protocol that utilises a complex set of attributes and policies to determine the best path for routing between autonomous systems (ASes).
- b) BGP is a routing protocol to establish secure VPN connections between network devices.
- c) BGP resolves domain names to IP addresses in the DNS hierarchy.
- **d) BGP is an exterior gateway protocol to exchange routing information between autonomous systems (ASes).**

### 13. Which protocol typically uses path vector protocol?

- a) OSPF (Open Shortest Path First)
- **b) BGP (Border Gateway Protocol)**
- c) MPLS (Multiprotocol Label Switching)
- d) RIP (Routing Information Protocol)

### 14. Which statement accurately describes Software-Defined Networking (SDN)?

- **a) SDN is a networking approach that separates the control plane from the data plane, allowing centralised management and programmability of network resources.**
- b) SDN is a protocol for secure communication between servers and clients in a network environment.
- c) SDN is a network security framework that prevents unauthorised access to network devices.
- d) SDN is a protocol used for load balancing and traffic distribution across multiple servers in a data center.

### 15. What role does Ansible play in the realm of IT automaƟon?

- a) Ansible is a scripting language used for developing web applications.
- b) Ansible is a virtualisation platform for managing and orchestrating virtual machines.
- **c) Ansible is a configuration management tool that enables automated provisioning, deployment, and IT infrastructure management.**
- d) Ansible is a database management system for storing and retrieving structured data

### 16. Which message format is typically used in RESTCONF (RESTful Configuration Protocol) for exchanging data between clients and network devices?

- **a) JSON (JavaScript Object Notation)**
- b) XML (eXtensible Markup Language)
- c) YAML (YAML Ain't Markup Language)
- d) HTML (Hypertext Markup Language)

---

## Section B: Short Answer Questions (12 Points)

### 1. Explain the role that monitoring plays in supporting FCAPS.

Monitoring is crucial in FCAPS (Fault, Configuration, Accounting, Performance and Security Management) as it helps in detecting and resolving system failures, verifying and tracking configurations, collecting usage statistics for billing and auditing, ensuring Quality of Service (QoS) by measuring network performance metrics and enhancing security by analyzing logs and issuing alerts for unexpected activities.

Effective monitoring ensures that each FCAPS function operates efficiently and reliably.



### 2. Provide two examples of internal and external routing protocols. Briefly describe their differences and why external is more adequate for the Internet.
Examples of internal routing protocols are:
    - OSPF (Open Shortest Path First)
    - RIP (Routing Information Protocol)

Examples of external routing protocols are:
    - BGP (Border Gateway Protocol)
    - EGP (Exterior Gateway Protocol)


**Internal Routing/Gateway Protocols (IGPs)** are routing protocols that are used within a single organization (Autonomous System) and are usually administered by a single entity.
**External Routing/Gateway Protocols (EGPs)** are routing protocols that are by various organizations (Autonomous System) and are typically within more than one administrative domain. They are the routing protocols that "glue" the various AS's in the Internet and each node is usually managed by a different entity.

Exterior Routing Protocols such as BGP are more adequate for the internet since they are designed to handle a complex and large-scale interconnecting variety of Autonomous Systems (ASes).
These protocols ensure efficient and scalable routing between these autonomous systems allowing for dynamic and flexible/configurable path selection, policy enforcement and fault tolerance. BGP is in particular adaptable, supporting policy-based routing and enabling networks to make informed decisions based on various routing policies and preferences, which is crucial for maintaining the stability and reliability of the internet.


### 3. What is the role of a DNS resolver in the domain name resolution process?

A DNS resolver is the first DNS server that is accessed when a DNS Query is made. The DNS Resolver then checks it cache and, if it has the requested name on it, sends the DNS response to the respective client. If the resolver does not have the name cached, it queries the appropriate root server, which will then forward the request to the right Top-Level-Domain and Second-Level-Domain if needed. When the name is finally resolved to the right ip value, an answer will be sent to the DNS resolver and it will cache it and then send the answer to the client.

By caching the names, the DNS resolver reduces the load on the authorative servers and enhances the scalability of the DNS System.


### 4. Why was DevOps introduced in the software development cycle?

DevOps was introduced to eliminate silos between development and operations teams. Silos create inefficiencies and slow down problems resolution because specialized teams (e.g., dev and operations) need to coordinate extensively. DevOps fosters collaboration by integrating members with both development and operations expertise within the same team. This integration accelerates the software developmente lifecycle, improves problem-solving and enhances the overall efficiency of the members, since they have a wider perspective of the given problem.
DevOps teams are also more resilient and can recover quickly from failures, promoting a culture of continues improvement and rapid iteration.



### 5. What are the features of (Software-Defined Networking) SDN?
SDN's (Software-Defined Networks) main features are:

- Scalability: By passing the control network devices control plane responsibilities (either all of them or a part) to the SDN controller, each device has fewer responsibilities, making the network is easier to scale
- Visibility: sdn promotes enhanced visibility of the entire network, aiding monitoring, troubleshooting and maintaining Quality of Service (QoS).
- Security: Applying security patches becomes easier, since they can be applied directly on the centralized controller. Also, since there is more visibility over the network, identifying security problems becomes easier.
- Modifiability: Network changes can be done programatically via the Northbound Interface (NBI).
- Automation: making automation if network configuration and tasks easier and reducing manual intervention.
- Vendor-neutral: SDN promotes interoperability between devices despite their vendor or hardware by making usage of open standards and APIs.


### 6. Describe the relationship between NETCONF (Network Configuration Protocol) and YANG (Yet Another Next Generation) in the context of network management.
YANG is a data modeling language that defines a structured and consistent format for network configuration and state data. 
NETCONF is a protocol that uses mainly XML and YANG data models to enable automated communication with network devices. NETCONF leverages YANG models to provide a standardized, manufacturer-neutral way to configure, monitor and manage network devices, making it really popular for scripting and SDNS (Software Defined Networking) environments. Together, thet facilitate efficient and scalable network management by ensuring interoperability and automation. 
