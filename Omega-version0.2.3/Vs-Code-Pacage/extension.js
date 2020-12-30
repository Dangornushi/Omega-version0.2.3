const vscode = require("vscode");

const OREORE_MODE = { scheme: 'file', language: "omega" };


class OreoreCompletionItemProvider {
    provideCompletionItems(document, position, token) {
        const completionItems = [
            {
                label: 'def',
                kind: vscode.CompletionItemKind.Variable
            },
            {
                label: 'let',
                kind: vscode.CompletionItemKind.Value
            },
            {
                label: 'if',
                kind: vscode.CompletionItemKind.Value
            },
            {
                label: 'str',
                kind: vscode.CompletionItemKind.Method
            }
        ];
        let completionList = new vscode.CompletionList(completionItems, false);
        return Promise.resolve(completionList);
    }
}

class OreoreHoverProvider {
    provideHover(document, position, token) {
        let wordRange = document.getWordRangeAtPosition(position, /[a-zA-Z0-9_]+/);
        if (wordRange === undefined) return Promise.reject("no word here");

        let currentWord = document.lineAt(position.line).text.slice(wordRange.start.character, wordRange.end.character);
        if (currentWord === "def") return Promise.resolve(new vscode.Hover("関数定義[define]"));
        if (currentWord === "if") return Promise.resolve(new vscode.Hover("条件分岐[  if  ]"));
        return Promise.resolve(new vscode.Hover(currentWord));
    }
}

function formatfile(textEditer, textEditerEdit) {
    const wholeText = textEditer.document.getText();
    const newwholeText = wholeText.split(/\r?\n/).map(line => line.replace(/^\s+/, "")).join("\n");

    const wholeRange = new vscode.Range(
        textEditer.document.positionAt(0),
        textEditer.document.positionAt(wholeText.newwholeText));
        textEditer.edit(editBuilder => editBuilder.replace(wholeRange, newwholeText));
}

function helloworld() {
    vscode.window.showInformationMessage("Hello, World!!");
}

function activate(context) {
    context.subscriptions.push(vscode.commands.registerCommand("omega.test", helloworld));
    context.subscriptions.push(vscode.commands.registerTextEditorCommand("omega.formatfile", formatfile));
    context.subscriptions.push(vscode.languages.registerHoverProvider(OREORE_MODE, new OreoreHoverProvider()));
    context.subscriptions.push(vscode.languages.registerCompletionItemProvider(OREORE_MODE, new OreoreCompletionItemProvider(), '.'));
}

function deactivate() {
    return undefined;
}

module.exports = { activate, deactivate };
