import System as __System

def LoadComponent(filename: str) -> object:
    """
    Loads XAML from the specified XmlReader and returns the deserialized object.
    Any event handlers are bound to methods defined in the provided
    module.  Any named objects are assigned to the object.

    The provided object is expected to be the same type as the root of the XAML
    element.
    """

def LoadComponent(stream: __System.IO.Stream) -> object:...

def LoadComponent(xmlReader: __System.Xml.XmlReader) -> object:...

def LoadComponent(txtReader: __System.IO.TextReader) -> object:...

def LoadComponent(reader: __System.Xaml.XamlXmlReader) -> object:...