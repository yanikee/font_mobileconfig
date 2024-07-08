import base64
import os
import uuid

def font_to_mobileconfig(font_path, output_path, font_name):
    with open(font_path, 'rb') as font_file:
        encoded_font = base64.b64encode(font_file.read()).decode('utf-8')
    
    payload_uuid = str(uuid.uuid4())
    font_payload_uuid = str(uuid.uuid4())
    
    mobileconfig_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>PayloadType</key>
            <string>com.apple.font</string>
            <key>PayloadIdentifier</key>
            <string>com.example.font.{font_name}</string>
            <key>PayloadUUID</key>
            <string>{font_payload_uuid}</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
            <key>PayloadDisplayName</key>
            <string>{font_name}</string>
            <key>Name</key>
            <string>{font_name}</string>
            <key>Font</key>
            <data>
{encoded_font}
            </data>
        </dict>
    </array>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadIdentifier</key>
    <string>com.example.profile</string>
    <key>PayloadUUID</key>
    <string>{payload_uuid}</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
    <key>PayloadDisplayName</key>
    <string>Font Profile</string>
</dict>
</plist>
"""
    with open(output_path, 'w') as mobileconfig_file:
        mobileconfig_file.write(mobileconfig_content)

    print(f"{output_path} has been created successfully.")

def main():
    font_path = input("フォントファイルのパスを入力してください: ").strip()
    output_path = input("出力するmobileconfigファイルのパスを入力してください: ").strip()
    font_name = input("フォントの名前を入力してください: ").strip()
    
    font_to_mobileconfig(font_path, output_path, font_name)

if __name__ == "__main__":
    main()
