import json
import random
import os



key_list = ["1.  X  layer_1_physical", "2.  X layer_2_data_link", "3.  X layer_3_network",
            "4.  X layer_4_transport", "5.  X layer_5_session",
            "6.  X layer_6_presentation", "7.  X layer_7_application"]


y = 0
layers = {

    "layer_1_physical": {
        "name": "layer_1_physical",
        "info": "Signaling, cabling, connectors, problems - fix cabling, punch-downs, etc, run loopback, test/replace "
                "cables, swap adapter cards.",
        "real-world osi": "- Cables, fiber, and the signal itself",
        "Follow the conversation": "Physical: Electrical signals",
    },
    "layer_2_data_link": {
        "name": "layer_2_data_link",
        "info": "The basic network language, foundation of communication, data link control (DLC), protocols -mac (media access control) address on ethernet, the switching layer",
        "real-world osi": "Frame, MAC address, Extended Unique identifier (EUI-48, EUI-64),Switch",
        "Follow the conversation": "Data Link: Ethernet",
    },
    "layer_3_network": {
        "name": "layer_3_network",
        "info": "the 'routing' layer, internet protocol(IP), Fragments frames to traverse different, networks",
        "real world osi": "IP Address, Router, Packet",
        "Follow the conversation": "Network: IP encapsulation",
    },
    "layer_4_transport": {
        "name": "layer_4_transport",
        "info": "The 'post office' layer,-Parcels and letters, TCP: (Transmission Control Protocol) ,UDP: (User Datagram protocol)",
        "real world osi": "TCP segment, UDP datagram",
        "Follow the conversation": "Transport: TCP encapsulation",
    },
    "layer_5_session": {
        "name": "layer_5_session",
        "info": "Communication management between devices, -start, stop, restart, control protocols, tunneling "
                "protocols",
        "real world osi": "Control protocols, tunneling protocols",
        "Follow the conversation": "Session: Link the presentation to the transport",
    },
    "layer_6_presentation": {
        "name": "layer_6_presentation",
        "info": "Character encoding, Application encryption, Often combined with the Application Layer",
        "real world osi": "Application encryption (SSL/TLS)",
        "Follow the conversation": "Presentation: SSL encryption",
    },
    "layer_7_application": {
        "name": "layer_7_application",
        "info": "The layer we see, HTTP, FTP, DNS, POP3",
        "real world osi": "Your eyes",
        "Follow the conversation": "Application: httpsL//mail.google.com",
    }
}
layer_list = [json.dumps(layers["layer_1_physical"]["info"]), json.dumps(layers["layer_2_data_link"]["info"]), json.dumps(layers["layer_3_network"]["info"]),
              json.dumps(layers["layer_4_transport"]["info"]), json.dumps(layers["layer_5_session"]["info"]), json.dumps(layers["layer_6_presentation"]["info"]), json.dumps(layers["layer_7_application"]["info"])]
random_info = random.choice(layer_list)
def display_list():
    for i in key_list:
        print(i)

def numbered_osi_keys():
    while y == 0:
        random_info = random.choice(layer_list)
        print(random_info)
        display_list()
        ask = int(input("Pick number that best matches sentence?\n"))
        if ask == 1:
            if random_info == layer_list[0]:
                key_list[0] = "1.  Correct  layer_1_physical"
                display_list()
        if ask == 2:
            if random_info == layer_list[1]:
                key_list[1] = "2.  Correct layer_2_data_link"
                display_list()
        if ask == 3:
            if random_info == layer_list[2]:
                key_list[2] = "3.  Correct layer_3_network"
                display_list()
        if ask == 4:
            if random_info == layer_list[3]:
                key_list[3] = "4.  Correct layer_4_transport"
                display_list()
        if ask == 5:
            if random_info == layer_list[4]:
                key_list[4] = "5.  Correct layer_5_session"
                display_list()
        if ask == 6:
            if random_info == layer_list[5]:
                key_list[5] = "6.  Correct layer_6_presentation"
                display_list()
        if ask == 7:
            if random_info == layer_list[6]:
                key_list[6] = "7.  Correct layer_7_application"
                display_list()

numbered_osi_keys()