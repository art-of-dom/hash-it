#!/bin/bash

set -e
set -x

FILE_INPUT="test/support/example.bin"
ASCII_INPUT="123456789"
HEX_INPUT="010203040506070809"
CMD_BASE="python -m hashit"

# array of supported hashes
declare -a HASHES=("CRC8" "CRC16" "CRC32" "CRC64" "MD5" "SHA1" "SHA224" "SHA256" "SHA384" "SHA512")

declare -A FILE_VERIFY=(["CRC8"]="14" ["CRC16"]="BAD3" ["CRC32"]="29058C73" ["CRC64"]="6C27EAA78BA3F822"
    ["MD5"]="E2C865DB4162BED963BFAA9EF6AC18F0" ["SHA1"]="4916D6BDB7F78E6803698CAB32D1586EA457DFC8"
    ["SHA224"]="88702E63237824C4EB0D0FCFE41469A462493E8BEB2A75BBE5981734"
    ["SHA256"]="40AFF2E9D2D8922E47AFD4648E6967497158785FBD1DA870E7110266BF944880"
    ["SHA384"]="FFDAEBFF65ED05CF400F0221C4CCFB4B2104FB6A51F87E40BE6C4309386BFDEC2892E9179B34632331A59592737DB5C5"
    ["SHA512"]="1E7B80BC8EDC552C8FEEB2780E111477E5BC70465FAC1A77B29B35980C3F0CE4A036A6C9462036824BD56801E62AF7E9FEBA5C22ED8A5AF877BF7DE117DCAC6D")

declare -A ASCII_VERIFY=(["CRC8"]="F4" ["CRC16"]="BB3D" ["CRC32"]="CBF43926" ["CRC64"]="46A5A9388A5BEFFE"
    ["MD5"]="25F9E794323B453885F5181F1B624D0B" ["SHA1"]="F7C3BC1D808E04732ADF679965CCC34CA7AE3441"
    ["SHA224"]="9B3E61BF29F17C75572FAE2E86E17809A4513D07C8A18152ACF34521"
    ["SHA256"]="15E2B0D3C33891EBB0F1EF609EC419420C20E320CE94C65FBC8C3312448EB225"
    ["SHA384"]="EB455D56D2C1A69DE64E832011F3393D45F3FA31D6842F21AF92D2FE469C499DA5E3179847334A18479C8D1DEDEA1BE3"
    ["SHA512"]="D9E6762DD1C8EAF6D61B3C6192FC408D4D6D5F1176D0C29169BC24E71C3F274AD27FCD5811B313D681F7E55EC02D73D499C95455B6B5BB503ACF574FBA8FFE85")

$CMD_BASE -f "$FILE_INPUT"
$CMD_BASE -a "$ASCII_INPUT"
$CMD_BASE -x "$HEX_INPUT"

for hash in "${HASHES[@]}"
do
    echo "Using hash $hash"

    $CMD_BASE -f "$FILE_INPUT" --hash-type "$hash"
    $CMD_BASE -a "$ASCII_INPUT" --hash-type "$hash"
    $CMD_BASE -x "$HEX_INPUT" --hash-type "$hash"

    $CMD_BASE -rf "$FILE_INPUT" --hash-type "$hash"
    $CMD_BASE -ra "$ASCII_INPUT" --hash-type "$hash"
    $CMD_BASE -rx "$HEX_INPUT" --hash-type "$hash"

    if [[ -v "FILE_VERIFY[$hash]" ]] ; then
        $CMD_BASE -f "$FILE_INPUT" --hash-type "$hash" --verify "${FILE_VERIFY[$hash]}"
    fi

    if [[ -v "ASCII_VERIFY[$hash]" ]] ; then
        $CMD_BASE -a "$ASCII_INPUT" --hash-type "$hash" --verify "${ASCII_VERIFY[$hash]}"
    fi
done

