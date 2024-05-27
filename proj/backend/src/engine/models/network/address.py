"""
"""


class IPAddress:
    """ """

    def __init__(self, address: str):
        self.address = address

    def _as_number(self) -> int:
        """
        Returns the number corresponding to this address.

        Returns:
            int: the number corresponding to this address
        """

        part1, part2, part3, part4 = self.address.split(".")

        return (
            (int(part1) * 256 ** 3) + (int(part2) * 256 ** 2) + (int(part3) ** 256) + int(part4)
        )

    def __gt__(self, other: "IPAddress") -> bool:
        """
        Checks if this address is greater than another address.

        Args:
            other (IPAddress): the address to check against

        Returns:
            bool: whether this address is greater than the specified address
        """

        return self._as_number() > other._as_number()

    def __le__(self, other: "IPAddress") -> bool:
        """
        Checks if this address is less than or equal to another address.

        Args:
            other (IPAddress): the address to check against

        Returns:
            bool: whether this address is less than or equal to the specified address
        """

        return not self > other

    def __add__(self, offset: int) -> "IPAddress":
        """Adds the given offset to this address, returning the corresponding IPAddress

        Args:
            offset (int): the offset to add

        Returns:
            IPAddress: the address distanced <offset> from this address
        """

        self_as_number = self._as_number()

        final_address_number = self_as_number + offset

        part4 = final_address_number % 256
        part3 = (final_address_number // 256) % 256
        part2 = (final_address_number // 256 ** 2) % 256
        part1 = (final_address_number // 256 ** 3) % 256

        return IPAddress(f"{part1}.{part2}.{part3}.{part4}")

    @staticmethod
    def from_string(address_str: str) -> "IPAddress":
        """_summary_

        Args:
            cidr_string (str): _description_

        Returns:
            IPAddress: _description_

        Raises:
            ValueError: _description_
        """

        if not address_str:
            raise ValueError("CIDR string cannot be empty")

        return IPAddress(address_str)

    def __str__(self) -> str:
        """ """

        return self.address

    def __repr__(self) -> str:
        """ """

        return self.address


class CIDR:
    """ """

    def __init__(self, base_address: IPAddress, mask_size: int) -> None:
        """ """

        self.base_address = base_address
        self.mask_size = mask_size

    def __contains__(self, address: IPAddress) -> bool:
        """
        Checks if this CIDR address range contains the given address

        Args:
            address (IPAddress): the address to check

        Returns:
            bool: whether the given address belongs to this address range or not
        """

        return (
            self.base_address
            <= address
            <= (self.base_address + 2 ** (32 - self.mask_size))
        )

    def contains(self, address: IPAddress) -> bool:
        """Checks if the given address is part of this address range, denoted in CIDR notation.

        Args:
            address (IPAddress): the address to verify

        Returns:
            bool: whether the given address is in the range given by this CIDR address range.
        """

        return address in self

    @staticmethod
    def from_string(cidr_str: str) -> "CIDR":
        """_summary_

        Args:
            cidr_string (str): _description_

        Returns:
            CIDR: _description_

        Raises:
            ValueError: _description_
        """

        if not cidr_str:
            raise ValueError("CIDR string cannot be empty")

        cidr_str = cidr_str.strip()

        if not cidr_str:
            raise ValueError("CIDR string cannot be empty")

        base_address, mask_size = cidr_str.split("/")

        return CIDR(
            base_address=IPAddress.from_string(base_address), mask_size=int(mask_size)
        )

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        return f"{self.base_address}/{self.mask_size}"

    def __repr__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        return f"{self.base_address}/{self.mask_size}"
