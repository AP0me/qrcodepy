<?php
$valid_hex_codes = [
  "1a2b3c",
  "4d5e6f",
  "7g8h9i"  // Add more valid hex codes as needed
];

$hex_code = isset($_GET['id']) ? $_GET['id'] : '';

if (in_array($hex_code, $valid_hex_codes)) {
  echo '
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Hex Code Validator</title>
    </head>
    <body>
      <h1>Hex Code Validator</h1>
      <div style="color: green;">The hex code is valid.</div>
    </body>
    </html>
  ';
} else {
  echo '
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Hex Code Validator</title>
    </head>
    <body>
      <h1>Hex Code Validator</h1>
      <div style="color: red;">The hex code is invalid.</div>
    </body>
    </html>
  ';
}
?>
