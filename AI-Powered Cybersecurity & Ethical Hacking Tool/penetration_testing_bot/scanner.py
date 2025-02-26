# scanner.py

import nmap
from scapy.all import sniff, TCP
import logging
from config import TARGET_IP, NETWORK_INTERFACE, LOG_FILE

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_network_scan(target):
    """Perform a network scan using Nmap."""
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-sV -O')
    
    for host in nm.all_hosts():
        logging.info(f"Host: {host}")
        logging.info(f"State: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            logging.info(f"Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                logging.info(f"Port: {port}, State: {nm[host][proto][port]['state']}, Service: {nm[host][proto][port]['name']}")

def analyze_network_traffic(packet):
    """Analyze network packets for suspicious behavior."""
    if packet.haslayer(TCP) and packet[TCP].dport == 80:
        logging.warning(f"Suspicious HTTP traffic detected: {packet.summary()}")

def run_penetration_test():
    """Main function to run the penetration tester."""
    logging.info("Starting Penetration Testing Bot...")
    
    # Run network scan
    run_network_scan(TARGET_IP)
    
    # Monitor network traffic
    sniff(iface=NETWORK_INTERFACE, prn=analyze_network_traffic, store=False)

if __name__ == "__main__":
    run_penetration_test()