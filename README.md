### Function app with HTTP trigger
This function app has an HTTP trigger that returns a message. 

### Prerequisites
- [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local#v2)
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
- [Azure Functions Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)

### Run the function app locally
1. Open the folder in Visual Studio Code.
2. Press `F5` to start the function app.
3. Open a web browser and navigate to `http://localhost:7071/api/hello?name=Azure`.
4. The browser displays a message: `Hello, Azure`.

### Deploy the function app to Azure
1. Sign in to Azure: `az login`.
2. Create a resource group: `az group create --name myResourceGroup --location westeurope`.
3. Deploy the function app: `func azure functionapp publish myFunctionApp --build-native-deps`.

### Test the function app in Azure
1. Open a web browser and navigate to `https://myFunctionApp.azurewebsites.net/api/hello?name=Azure`.
2. The browser displays a message: `Hello, Azure`.

### Clean up resources
1. Delete the resource group: `az group delete --name myResourceGroup`.

### Next steps
- [Azure Functions developer guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference)
- [Azure Functions triggers and bindings](https://docs.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings)
- [Azure Functions best practices](https://docs.microsoft.com/en-us/azure/azure-functions/functions-best-practices)