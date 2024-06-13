# Monitoring

## FCAPS - Review

| Component     | Explanation                                                                                                                                                       |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fault         | Recognize, isolate, correct and log faults in the network                                                                                                         |
| Configuration | Focus tracking and managing deployments in a centralized manner. Streamline device configuration and provisioning to ensure quicker configuration and flexibility |
| Accounting    | Gather usage statistics for users                                                                                                                                 |
| Performance   | Ensuring performance remains at acceptable levels                                                                                                                 |
| Security      | Controlling access to assets in the network                                                                                                                       |

## Monitoring

- **Get a sense of how the network is performing**
    - Make sure we're still offering a quality network
    - Essential for FCAPS

- **Short-term measurements**
    - Identify faults, congestions and attacks

- **Longer-term measurements**
    - Traffic engineering, e.g. reroute traffic or negociate new aggreements with peers
    - Upgrade link and device capacity

- **Accounting**
    - So you know how each client of the network is using the network

## Types of measurements

- Application and user-related measurements (e.g. web page loading times)
- Device measurements (e.g. CPU, memory usage, fan speed, etc.)
- Network measurements (e.g. traffic data, latency, throughput, routing data, etc.)

## Passive vs Active network measurements

- **Passive**
    - Get a sense of the existing traffic in the network
    - Have devices report how much traffic is going through (e.g. SNMP, netflow)
    - Tap a link or copy traffic to monitoring port (port mirroring)
    - For measuring production traffic and its carateristics

- **Active**
    - Inject new, measurement packets in the network
    - Get a sense of how the network reacts to this packets
    - Include responses (e.g. ICMP requests/replies for RTT)
    - For measuring the properties of the network (delay, jitter, topology, etc.)


The difference between passive and active network measurements is in their approach and purpose. Passive measurements involve observing and analyzing existing traffic without injecting additional packets, focusing on production traffic characteristics using methods like SNMP, NetFlow, or port mirroring. Active measurements, on the other hand, involve injecting test packets into the network to observe the network's behavior and properties, such as delay and jitter, using tools like ICMP requests/replies.

## Packet traces

- Motion-picture-like recording of everything that goes through the network
    - What, when, where, who, why

- Raw data - powerful but hard to use

- Difficult to manage
    - Capture and storage limitations

- Difficult to use and process
    - Not in a table like format
    - Can write processing rules to create tables – but only partial vision
    - AI and deep learning etc to process traces (raw or features)
    
## Traffic Counters (SNMP, etc.)

- Routers keep track of how much traffic goes through each link periodically (packets, bytes)
- Simple to use but limited in scope

## Traffic Matrices 

- Amount of data transmitted between every pair of nodes in the (rows and columns are the nodes in the network)

- Enterprise network, autonomous system
    - Points of Presence (PoP)
    - links between PoPs and PoPs and AS's (internal vs external traffic)

- Internal / External traffic matrix

## Flow measurement
- IP flows
    - Source, destination IP address and TCP/UDP ports (4 fields)
    - L3 header protocol (TCP, UDP, other)
    - other info

- Keeps record of traffic for each flow
    - Packet, byte count on each direction
    - Duration, first/last packet timestamps, TCP flags
    - etc.

- Tradeoff
    - simpler to use than packet traces
    - more information than counters
    - simply opening a web page can generate dozens of TCP flows

## What to do with measurement data?

- Store for later query and processing
    - Send to ELK, other big data storage
    - Plot charts, do queries on past data, correlate between different data sources
    - Build historical dataset for learning AI models for different management tasks

- Use immediately once data is generated
    - Anomaly detection and diagnostic, security, traffic engineering, …
    - Apply static rules, use pretrained AI models
    - Online learning, update AI model

## Other

### What's intserv?

IntServ, or Integrated Services, is an architecture designed to provide guaranteed Quality of Service (QoS) on IP networks. It achieves this by reserving resources along the data path and ensuring that applications receive the necessary bandwidth, latency, and reliability. IntServ uses protocols like RSVP (Resource Reservation Protocol) to signal and maintain resource reservations for individual data flows, thereby supporting applications that require specific performance levels, such as VoIP or video conferencing.

### What's traffic engineering?

Traffic engineering is the process of optimizing the performance and efficiency of a network by dynamically analyzing, predicting, and directing data traffic to avoid congestion and ensure efficient use of resources. It involves techniques such as load balancing, routing optimization, and the strategic allocation of bandwidth to improve overall network reliability, speed, and performance. The goal is to enhance user experience and meet service level agreements (SLAs) by managing data flows in a way that maximizes the utilization of network infrastructure while minimizing latency and packet loss.
