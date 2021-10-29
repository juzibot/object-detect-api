import Base64
using JSON3
using HTTP
b64s = Base64.Base64.base64encode(open("R-C.jpeg"))
req = `
    curl -XPOST http://localhost:12920/api/object-detect 
    -H 'Content-Type: applicaton/json' 
    -d '{"image": "$b64s"}'
`

HTTP.request(:POST, 
    "http://localhost:12920/api/object-detect", 
    ["Content-Type" => "applicaton/json"],
    JSON3.write(Dict("image" => b64s))) |> println
