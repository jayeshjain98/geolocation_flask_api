schema = {
        "type" : "object",
        "properties" : {
            "address" : {"type" : "string"},
            "output_format" : {"type" : "string", "enum" : ["json","Json","JSON","xml","Xml","XML"]}
        },
        "required" : ["address", "output_format"],
        "additionalProperties": False
}