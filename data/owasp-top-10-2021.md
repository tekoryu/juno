# OWASP Top 10 - 2021

The OWASP Top 10 is a standard awareness document for developers and web application security. It represents a broad consensus about the most critical security risks to web applications.

**Release Date:** September 2021

---

## A01:2021 - Broken Access Control

**Previous Ranking:** #5 (2017)

Broken Access Control vulnerabilities allow attackers to gain unauthorized access to user accounts, view sensitive data, or perform actions they shouldn't be allowed to. This moved to #1 in 2021 due to its prevalence and severity.

**Common Issues:**
- Bypassing access control checks by modifying URLs, internal application states, or HTML pages
- Allowing primary keys to be changed to access other users' records
- Elevation of privilege (acting as a user without being logged in, or acting as an admin when logged in as a user)
- Metadata manipulation such as replaying or tampering with JWT tokens
- CORS misconfiguration allowing unauthorized API access

---

## A02:2021 - Cryptographic Failures

**Previous Name:** Sensitive Data Exposure (2017)

This category focuses on failures related to cryptography which often lead to sensitive data exposure or system compromise.

**Common Issues:**
- Transmitting data in clear text (HTTP, FTP, SMTP)
- Using old or weak cryptographic algorithms or protocols
- Using default crypto keys, weak keys, or improper key management
- Not enforcing encryption (missing security directives or headers)
- Improperly validating certificates and trust chains
- Using deprecated hash functions (MD5, SHA1) for passwords

---

## A03:2021 - Injection

**Previous Ranking:** #1 (2017)

Injection flaws occur when untrusted data is sent to an interpreter as part of a command or query. This category now includes Cross-Site Scripting (XSS).

**Common Types:**
- SQL Injection
- NoSQL Injection
- OS Command Injection
- LDAP Injection
- Cross-Site Scripting (XSS)
- Expression Language (EL) or Object Graph Navigation Library (OGNL) Injection

**Impact:** Can result in data loss, corruption, disclosure, denial of access, or complete host takeover.

---

## A04:2021 - Insecure Design

**New Category in 2021**

Insecure Design represents missing or ineffective control design, distinct from insecure implementation. It focuses on risks related to design and architectural flaws.

**Key Points:**
- Focuses on threats modeled, design patterns, and reference architectures
- Requires secure development lifecycle, threat modeling, and secure design patterns
- Cannot be fixed by a perfect implementation (the design itself is flawed)
- Different from insecure implementation

**Examples:**
- Credential recovery flows without security questions or multi-factor authentication
- E-commerce sites allowing unlimited trial accounts for automated attacks
- Systems without rate limiting or resource exhaustion controls

---

## A05:2021 - Security Misconfiguration

**Previous Ranking:** #6 (2017)

Security misconfiguration is the most commonly seen vulnerability, often resulting from insecure default configurations, incomplete configurations, open cloud storage, misconfigured HTTP headers, and verbose error messages.

**Common Issues:**
- Missing appropriate security hardening
- Improperly configured permissions on cloud services
- Default accounts and passwords still enabled
- Overly detailed error messages revealing system information
- Latest security features disabled or not configured securely
- Security settings in application servers, frameworks, libraries not set to secure values
- Software out of date or vulnerable

---

## A06:2021 - Vulnerable and Outdated Components

**Previous Name:** Using Components with Known Vulnerabilities (2017)
**Previous Ranking:** #9 (2017)

Using components with known vulnerabilities can undermine application defenses and enable various attacks.

**Risk Factors:**
- Not knowing versions of components used (client-side and server-side)
- Software that is vulnerable, unsupported, or out of date
- Not scanning for vulnerabilities regularly
- Not fixing or upgrading the underlying platform, frameworks, and dependencies in a timely manner
- Developers not testing compatibility of updated libraries
- Not securing component configurations

---

## A07:2021 - Identification and Authentication Failures

**Previous Name:** Broken Authentication (2017)
**Previous Ranking:** #2 (2017)

Confirmation of user identity, authentication, and session management is critical. This category now includes CWEs related to identification failures.

**Common Issues:**
- Permits automated attacks such as credential stuffing
- Permits brute force or other automated attacks
- Permits default, weak, or well-known passwords
- Uses weak or ineffective credential recovery processes
- Uses plain text, encrypted, or weakly hashed passwords
- Missing or ineffective multi-factor authentication
- Exposes session identifiers in URLs
- Doesn't invalidate session IDs after logout or inactivity
- Fails to properly invalidate session IDs during login

---

## A08:2021 - Software and Data Integrity Failures

**New Category in 2021**

This category focuses on making assumptions related to software updates, critical data, and CI/CD pipelines without verifying integrity.

**Common Issues:**
- Applications relying on plugins, libraries, or modules from untrusted sources
- Insecure CI/CD pipelines introducing unauthorized access or malicious code
- Auto-update functionality downloading updates without integrity verification
- Insecure deserialization where untrusted data is used to inflict damage
- Objects or data encoded/serialized into a structure an attacker can modify

**Examples:**
- SolarWinds Orion attack
- Serialization attacks in Java, PHP, Python applications

---

## A09:2021 - Security Logging and Monitoring Failures

**Previous Name:** Insufficient Logging & Monitoring (2017)
**Previous Ranking:** #10 (2017)

Without logging and monitoring, breaches cannot be detected. Insufficient logging and monitoring coupled with missing or ineffective integration with incident response allows attackers to persist in systems.

**Common Issues:**
- Auditable events (logins, failed logins, high-value transactions) not logged
- Warnings and errors generate inadequate or unclear log messages
- Logs not monitored for suspicious activity
- Logs only stored locally
- Appropriate alerting thresholds and response escalation processes not in place
- Penetration testing and DAST scans don't trigger alerts
- Application unable to detect, escalate, or alert for active attacks in real-time

---

## A10:2021 - Server-Side Request Forgery (SSRF)

**New Category in 2021** (Added from community survey #1)

SSRF flaws occur when a web application fetches a remote resource without validating the user-supplied URL, allowing an attacker to coerce the application to send requests to unexpected destinations.

**Common Scenarios:**
- Attackers can access internal services behind firewalls
- Scan and attack systems from within the internal network
- Read local files using file:// protocol
- Access cloud service metadata endpoints
- Bypass access controls to sensitive endpoints

**Impact:** Can lead to unauthorized actions, data disclosure, or compromise of internal systems.

---

## References

- [OWASP Top 10:2021 Official Page](https://owasp.org/Top10/)
- [OWASP Foundation](https://owasp.org/)

## Notes

This document is based on the OWASP Top 10 - 2021 edition, released in September 2021. Organizations should use this as a starting point for establishing secure development practices and should also consider additional security requirements specific to their applications and environments.
