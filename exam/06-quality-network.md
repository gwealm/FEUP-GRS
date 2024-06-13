# Quality Network

## Challenges

-   Large number of devices, and switching limitations => capacity bottlenecks

-   Specific requirements for users and applications

    -   with service level commitments with users/clients

-   Costs

    -   **Capex**: Large expenditures that a company expects to influence production and profitability
    -   **Opex**: Daily, weekly, monthly and annual expenses that keep the organization running

-   Traffic Growth and shrinkage (possibly)

-   Network Outages

-   Users with different levels of access and accounts

-   Attacks

## The "dev | fence | ops" trap, configuration

-   Silos

    -   Network planning and design
    -   Network deployment

-   Devops for networking allows a more iterative process of design, deploy and getting feedback to update the network design

-   NFV helps

-   Cost of hardware and hardware compatibility with future network expansions

## Application quality requirements

-   **Capacity (bit/s)** - bandwidth intensive applications

    -   Bursts - timescale - how long, how many bytes

-   **Delay** - real time, interactive applications

    -   End-to-end delay (control)
    -   Round-trip delay (teleconference)
    -   Delay variation / jitter (visualization)

-   **Reliability** - mission critical applications
    -   Error rates - bit, packet, etc.
    -   Mean time between failures - MBTF
    -   Mean time to recover - MTTR
    -   Availability = MTBF / (MTBF + MTTR)
    -   Uptime(%) = 1 - Availability

## QoS and Traffic Engineering, SLA

-   **Best effort networks**

    -   Doesn't care about quality
    -   Serves packets by oredr of arrival
    -   Lightly used - Quality ok
    -   Heavily used - Quality degradation

-   **QoS**

    -   Queue management - choose packet, different queues
    -   Round-robin, token bucket, RED, etc - algorithms

-   **Tc linux**

-   **ATM, intserv, diffserv+MPLS**

## Faults

-   Both hardware and software faults exist

-   Root cause analysis - root cause detector is hard in complex networks

-   Fault recovery - agile configuration

-   Fault detection .signal processing and machine learning


## Security 

- **Enforncing Security**
    - Seggregation
    - Access Control
    - Firewall
    - IDS / IPS
    - ...

- **Security Management**
    - Vulnerability Scanning
    - Intelligence gathering
    - Incident response
    - Forensics
    - ...