language_detection
--------

To use, simply do::

    >>> from language_detection import language_detection
    >>> detector=language_detection()
	>>> print detector.language_list()  #list of supported languages
	>>> print detector.language_id(mytext)  #The language ID of input text
	>>> print detector.language_name(mytext)  #The language Name of input text
