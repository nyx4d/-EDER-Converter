async function loadAndExecuteBinary(filePath) {
    // Fetch the binary file
    const response = await fetch(filePath);
    const binaryData = await response.arrayBuffer();

    // Decode Base64 to string
    const decoder = new TextDecoder("utf-8");
    const jsCode = atob(decoder.decode(new Uint8Array(binaryData)));

    // Execute the decoded JavaScript
    eval(jsCode);
}

// Usage: Call with the path to the binary file
loadAndExecuteBinary('file:///C:/Users/nyx4d/dev3d/Python/js-to-bin/bin-v-%5E-js.js');
