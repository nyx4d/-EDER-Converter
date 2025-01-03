<?php
// Path to your .bin file
$binFilePath = 'three.bin';

if (file_exists($binFilePath)) {
    // Read the binary file
    $binaryData = file_get_contents($binFilePath);

    // Decode the Base64 encoded binary data back to JavaScript code
    $decodedJsCode = base64_decode($binaryData);

    // Set the appropriate headers
    header('Content-Type: application/javascript');

    // Send the decoded JavaScript code back to the client
    echo $decodedJsCode;
} else {
    http_response_code(404);
    echo 'Error: File not found';
}
?>
