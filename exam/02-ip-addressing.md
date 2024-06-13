# IP addressing

## Classes

-   First octet determines the class:
    -   00000000 => 0 (Class A)
    -   10000000 => 128 (Class B)
    -   11000000 => 192 (Class C)
    -   11100000 => 224 (Class D)
    -   11110000 => 240 (Class E)

| Class | Starting Addr | Ending Addr     | Usage        |
| ----- | ------------- | --------------- | ------------ |
| A     | 0.0.0.0       | 127.255.255.255 | Host Addr    |
| B     | 128.0.0.0     | 191.255.255.255 | Host Addr    |
| C     | 192.0.0.0     | 223.255.255.255 | Host Addr    |
| D     | 224.0.0.0     | 239.255.255.255 | Multicast    |
| E     | 240.0.0.0     | 255.255.255.255 | Experimental |

|         | 8 bits  | 8 bits  | 8 bits  | 8 bits | Network Mask |
| ------- | ------- | ------- | ------- | ------ | ------------ |
| Class A | Network | Host    | Host    | Host   | /8           |
| Class B | Network | Network | Host    | Host   | /16          |
| Class C | Network | Network | Network | Host   | /24          |

Class A: Large Companies\
Class B: Medium Sized Companies\
Class C: Homes

### Example

-   **1.2.3.4** - Class A

-   **191.200.100.1** - Class B

-   **192.168.1.1** - Class C

## Public vs Private IP

### Private IP Addresses

| Class | IP Address Range              | Default Subnet Mask |
| ----- | ----------------------------- | ------------------- |
| A     | 10.0.0.0 - 10.255.255.255     | 255.0.0.0           |
| B     | 172.16.0.0 - 172.31.255.255   | 255.0.0.0           |
| C     | 192.168.0.0 - 192.168.255.255 | 255.255.255.0       |

-   **Loopback:** 127.0.0.0/8

### Public IP Addresses

<table border="1" cellpadding="8" cellspacing="0">
    <tr>
        <th>Class</th>
        <th>Public IP Ranges</th>
    </tr>
    <tr>
        <td rowspan="2">A</td>
        <td>1.0.0.0 to 9.255.255.255</td>
    </tr>
    <tr>
        <td>11.0.0.0 to 126.255.255.255</td>
    </tr>
    <tr>
        <td rowspan="2">B</td>
        <td>128.0.0.0 to 171.255.255.255</td>
    </tr>
    <tr>
        <td>173.0.0.0 to 191.255.255.255</td>
    </tr>
    <tr>
        <td rowspan="2">C</td>
        <td>192.0.0.0 to 195.255.255.255</td>
    </tr>
    <tr>
        <td>197.0.0.0 to 223.255.255.255</td>
    </tr>
    <tr>
        <td rowspan="2">D</td>
        <td>224.0.0.0 to 247.255.255.255</td>
    </tr>
    <tr>
        <td>Multicast Addresses</td>
    </tr>
    <tr>
        <td rowspan="2">E</td>
        <td>248.0.0.0 to 255.255.255.254</td>
    </tr>
    <tr>
        <td>Experimental Use</td>
    </tr>
</table>

## Special Use Addresses

- **Host part all 0s:** network address
- **Host part all 1s:** broadcast address
- **0.0.0.0/8:** This network, this host (0.0.0.0)
- **127.0.0.0/8:** Loopback
- **169.254.0.0/16:, FE80:0:0:0:<Interface ID\>** Link local
- **10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16:** Private, NAT
- **224.0.0.0/4, FF::/8:** Multicast
- **FC00::/7:** unique local address (global id, subnet id, interface id)

## Magic Number Subnetting

-   **1.** Find the "interesting octet" (the number in the subnet mask that is not 0 or 255

-   **2.** Find the Magic Number

    -   Magic Number = 256 - "interesting octet"

-   **3.** Starting at 0, add magic number until you reach the number (without passing it)

    -   **Ban! Network Address**

-   **4.** Add Magic Number again

    -   **Bam! Next Network Address**

-   **5.** Take 1 away from the "interesting octet"

    -   **Bam! Broadcast Address**

-   **Note:** The number of hosts is **2 ^ (host bits) - 2**

-   **Note:** You can also calculate the magic number directly by checking the host bits

### Example: 16.25.123.15/19

Interesting octet: (third) 11100000 => 224

Magic Number = 256 - 224 = 32

32 + 32 + 32 = 96 ( + 32 = 128, PASSED 123)

Network Address: 16.25.96.0

96 + 32 - 1 = 127

Broadcast Address = 16.25.127.0

## Suppernetting - IP Aggregation

| CIDR       | /25 | /26 | /27 | /28 | /29 | /30 | /31 | /32 |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Subnet     | 128 | 192 | 224 | 240 | 248 | 252 | 254 | 255 |
| Group Size | 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |

-   Taking sub-networks and summar them into a single network.

- Supernetting for exact match by hand is only doable by manually calculating each subnet's range

### Supernetting to a single network

- **1.** Identify the **Smallest IP Address** and the **Largest IP Address**.

- **2.** Determine the **Group Size Increment** in relevant Octet which includes both.

#### Example:

- 9.9.168.192/26
- 9.9.162.0/23
- 9.9.170.160/27
- 9.9.167.0/24
- 9.9.167.128/25

**Smallest IP:** 9.9.162.0

**Largest IP:** 9.9.170.192

**Increment Needed:** 170 - 162 = 8 (2^3 aka /21)

Since 9.9.160.0/21 doesn't fit both the addresses and the next /21 (9.9.168.0/21) doesn't fit too, we need a /20 network: ** **9.9.160.0/20**
