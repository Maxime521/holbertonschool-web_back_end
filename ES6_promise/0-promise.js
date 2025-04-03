/*eslint-disable */
export default function getResponseFromAPI() {
    // Return a new Promise
    return new Promise((resolve, reject) => {
      // Simulate an asynchronous operation (e.g., API call)
      setTimeout(() => {
        const success = true; // Simulate success or failure
        if (success) {
          resolve("Response from the API");
        } else {
          reject(new Error("Failed to fetch response from the API"));
        }
      }, 1000); // Simulate a delay of 1 second
    });
}
