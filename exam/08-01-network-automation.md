Network automation provides various benefits:

- Human error is reduced

- Networks become much more scalable (new deployments, network-wide changes and troubleshooting can be implemented in a fraction of time)

- Network-wide policy compliance can be assured (standard configurations software versions, etc.)

- The improved efficiency of network operations reduces the opex (operating expenses) of the network. Each task requires fewer man-hours.

#### What does a router to?
- It forwards messages between networks by examining information in the Layer 3 header.
- It uses a routing protocol like OSPF to share route information with other routers and build a routing table.
- It uses ARP to build an ARP table, mapping IP addresses to MAC addresses.
- It uses Syslog to keep logs of events that occur.
- It allows a user to connect to it via SSH and manage it.

#### What does a router to?
- It forwards messages within a LAN by examining information in the Layer 2 header.
- It uses STP to enure there are no Layer 2 loops in the network.
- It builds a MAC address table by examining the source MAC address of frames.
- It uses Syslog to keep logs of events that occur.
- It allows users to connect to it via SSH and manage it.

The various functions of network devices can be logically divided up (categorized) into planes:
- Data plane
- Control plane
- Management plane

###  Data plane (aka forwarding plane)

- All tasks involved in forwarding user data/traffic from one interface to another are part of the data plane.
- A router receives a message, looks for the most specific matching route in its routing table and forwards it out the appropriate interface to the next hop.
    - It also de.encapsulates the original layer 2 header and re-encapsulates with a new header destined for the next hop's MAC address.

- A switch receives a message, looks at the destination MAX address, and forwards it out of the appropriate interface (or floods it).
    - This includes functions like adding or removing 802.1q VLAN tags

- NAT (changing the src/dst addresses before forwarding) is part of the data plane

- Deciding to forward or discard messages due to ACLs, port security, etc. is part of the data plane.

- The data plane is the reason we buy routers and switches (and network infrastructure in general), to forward messages. However, the Control plane and Management plane are both necessary to enable the data plane to do its job.

- ASIC (Application-Specific Integrated Circuits) are used, because CPU processing is slow.
    - When a frame is received the ASIC is responsible for the switching logic
    - The MAC address table is stored in a kind of memory called TCAM (Ternary Content-Adressable Memory) -> allows for very fast lookups
    - The ASIC feeds the destination MAC address of the frame into the TCAM, which returns the matching MAC address table entry (aka CAM table entry)


### Control Plane

- How does a device's data plane make its forwarding decision?
    - routing table, MAC address table, ARP table, STP, etc.

- Functions that build these tables (and other functions that influence the data plane) are part of the control plane.

- The control plane controls what the data plane does, for example, by building the router's routing table.

- The control plane performs overhead work.
    - OSPF itself doesn't forward user data packets, but it informs the data plane about how packets should be forwarded.
    - STP itself isn't involved in the process of forwarding frames, but it informs the data plane about which interfaces should and shouldn't be used to forward frames.
    - ARP messages aren't user data, but they are used to build an ARP table which is ussed in the process of forwarding data.

---

- **In traditional networking the data plane and control plane are both distributed. Each device has its own data plane and its own control plane. The planes are "distributed" throughout the network.** => this is different from SDNS

### Management Plane

- Like the control plane, the management plane performs overhead work.
    - However, the management plane doesn't directly affect the forwarding of messages in the data plane.

- The management plane consists of protocols that are used to manage devices.
    - SSH/Telnet, used to connect to the CLI of a device to configure/manage it.
    - Syslog, used to keep logs of events that occur on the device.
    - SNMP, used to monitor the operations and status of the device.
    - NTP, used to maintain accurate time on the device. 
