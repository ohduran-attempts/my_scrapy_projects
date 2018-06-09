# XPath

## List of XPath

### Starts with //
If the path starts with // then all elements in the document which fullfill following criteria are selected.

### Starts with /
If the path starts with the slash / then it represents an absolute path to the required element.

### All elements: *
The star * selects all elements located by preceeding path, like `//*`.

### Further condition inside
Expression in square brackets [] can further specify an element. A number in the brackets gives the position of the element in the selected set. The function last() selects the last element in the selection:

`/AAA/BBB[1]`

`/AAA/BBB[last()]`

### Attributes
Attributes are specified by @ prefix.

//@id

//BBB[@id]

//BBB[@name]

//BBB[@*]

//BBB[not(@*)]

### Attribute values
Values of attributes can be used as selection criteria. Function normalize-space removes leading and trailing spaces and replaces sequences of whitespace characters by a single space.

//BB[@id='b1']

//BBB[@name='bbb']

//BBB[normalize-space(@name)='bbb']

### Nodes counting
Function count() counts the number of selected elements

//*[count(BBB)=2]

//BBB[count(*)=2]

//*[count(*)=3]

### Descendant axis
Contains the descendants of the context node; a descendant is a child or a child of a child and so on; thus, the descendant axis never contains attribute or namespace nodes.

/descendant::*

/AAA/BBB/descendant::*

//CCC/descendant::*

//CCC/descendant::DDD

### Descendant or self axis
The descendant or self axis contains the context node and the descendants of the context node

/AAA/XXX/descendants-or-self::*

//CCC/descendants-or-self::*
