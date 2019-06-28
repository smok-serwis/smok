This document describes the basic ideas behind the SMOK API.

# Device

While working as a Device, you are expected to feed the SMOK API with values of your
pathpoints. Pathpoints have a type, specified by it's first character:

* *w* - signed word
* *W* - unsigned word
* *B* - boolean, 0 or 1
* *f* - a float
* *u* - an Unicode

And then the list of further characters comes into play. So, a pathpoint is basically
defined by it's type and pathname, of which first character describes it's type.

Such a list of Pathpoints is known in advance by the Server, and it's the Server
that's the single source of authority on what Pathpoints does a given Device support.

However, it's the duty of the Device to register Pathpoints for example for commands
received by the server. A basic command concerns a request to read the current value
from given Pathpoint, or to write a value of a given Pathpoint with a server-provided
value, as part of executing orders executed by the user or an autonomous service
running as part of SMOK's infrastructure.