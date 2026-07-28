# WriteUp - Old Target

## Overview

* **Name:** Old Target
* **Category:** SIEM
* **Point:** 250
* **Author:** aseng
* **Desc:** 
````
This is a series of SOC LKSP, for the attachment password is G/IcUCaGcc5T/cejOaf7hCLcyhuOainUBCwWPNa7h50= . Please use SIEM to answer this challenge!

There's a targeted AD attack in July 2025. I need you to gather some basic questions for your finale.

What's the NetBIOS domain name of the active directory?

Example: If you found the domain name is haka.LOCAL then the NetBIOS name is HAKA. Wrap it with LKS{haka}.
````


* **File:** [SOC_DIST.zip](./SOC_DIST.zip)

## Summary

NetBIOS Domain is a short name (legacy name) used by the old NetBIOS/SMB protocol to identify a Windows domain or workgroup.

Example:

| Active Directory Domain | NetBIOS Domain |
| ----------------------- | -------------- |
| `corp.example.com`      | `CORP`         |
| `lab.local`             | `LAB`          |
| `contoso.com`           | `CONTOSO`      |

the NetbiOS actualy same with hostname because the hostname not join any Active Directory. So Windows use hostname as NetBIOS.

Hostname = DESKTOP-7F2A91
NetBIOS Name  : DESKTOP-7F2A91

<b>FLAG:
----
LKS{setiabudi}
</b>
