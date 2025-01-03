# -EDER-Converter  ||  Author: Nyx4D
Encode => Decode => Execute => Remove

JavaScript Binary Converter and Dynamic Loader

This project demonstrates how to securely encode sensitive JavaScript functions into a binary format using Python, dynamically load them from a server using PHP and JavaScript, decode them on the client side, and execute them. After execution, the JavaScript is removed to enhance security.

JavaScript Binary Converter and Dynamic Loader

Author: Nyx4D

This project demonstrates how to securely encode sensitive JavaScript functions into a binary format using Python, dynamically load them from a server using PHP and JavaScript, decode them on the client side, and execute them. After execution, the JavaScript is removed to enhance security.
Features

    Python-based Converter: Converts JavaScript files into binary format for secure storage.
    PHP Decoder: Decodes binary files on the server and delivers JavaScript to the client.
    Dynamic Execution: Loads, executes, and removes JavaScript on demand.
    Improved Security: Ensures sensitive JavaScript is not stored as plain text on the server or visible in the browser dev tools.

How It Works

    Binary Conversion with Python: Use the Python script to convert your JavaScript files into binary format.

    Server Storage: Store the .bin files on a server (can be on a separate domain for added security).

    Dynamic Decoding: Use a PHP script to decode the binary files back to JavaScript format on the fly.

    Client Execution: Load and execute the decoded JavaScript dynamically using AJAX.

    Cleanup: Remove the decoded JavaScript after execution to prevent exposure.

Setup Instructions
Prerequisites

    Python 3.x
    A web server with PHP support (e.g., Apache, Nginx)
    A browser that supports modern JavaScript features

Step 1: Convert JavaScript to Binary

    Navigate to the python/ directory.
    Run the Python script:

    python js_to_bin_converter.py

    Select a .js file to encode. The script will generate a .bin file in the same directory.

Step 2: Upload Binary File to Server

    Place the .bin file in the server/ directory on your web server.
    Ensure the decode_js.php script is also in the same directory.

Step 3: Integrate into HTML

    Add the following JavaScript function to your client/main.js:

async function loadAndExecuteBinary(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`Failed to load: ${response.statusText}`);
        const jsCode = await response.text();
        const script = document.createElement('script');
        script.textContent = jsCode;
        document.body.appendChild(script);
        console.log('Script executed successfully.');
        document.body.removeChild(script);
    } catch (error) {
        console.error('Error:', error);
    }
}

Call the function in your index.html:

    loadAndExecuteBinary('https://yourserver.com/decode_js.php?file=three.bin');

Step 4: Run the Application

    Open client/index.html in your browser.
    Watch the dynamically loaded JavaScript execute and render the output.

Example Workflow

    Use the Python script to convert three.js into three.bin.
    Upload three.bin to your server.
    Use the JavaScript function to dynamically load and execute the binary file:

    loadAndExecuteBinary('https://example.com/server/decode_js.php?file=three.bin');

    After execution, the script is removed from the DOM.

Security Notes

    Ensure your PHP script is secure and does not allow arbitrary file access.
    Use HTTPS to prevent interception of sensitive JavaScript during transfer.
    Consider additional obfuscation techniques for sensitive logic.

Contributing

Feel free to fork this repository and make improvements. Pull requests are welcome! 🛠️
License

This project is licensed under the MIT License. See the LICENSE file for details.

Email: nyx4d@proton.me
