// Captura de ecran a unei pagini, prin WKWebView.
//
// Nu exista Chrome pe masina asta, deci nu merge `--headless --screenshot`.
// Safari/WebKit exista insa in sistem, iar Xcode da compilatorul Swift, asa ca
// randam pagina intr-un WKWebView invizibil si salvam un PNG.
//
// Folosire:
//   swift unelte/captura.swift <url> <fisier.png> [latime] [inaltime]
//
// Inaltimea 0 inseamna "toata pagina": masuram document.body.scrollHeight dupa
// incarcare si redimensionam vederea inainte de captura.

import Cocoa
import WebKit

let argumente = CommandLine.arguments
guard argumente.count >= 3 else {
    FileHandle.standardError.write("folosire: captura.swift <url> <iesire.png> [lat] [inalt]\n".data(using: .utf8)!)
    exit(2)
}
let adresa = argumente[1]
let iesire = argumente[2]
let latime = argumente.count > 3 ? Int(argumente[3]) ?? 1440 : 1440
let inaltimeCeruta = argumente.count > 4 ? Int(argumente[4]) ?? 0 : 0

final class Fotograf: NSObject, WKNavigationDelegate {
    let vedere: WKWebView
    let iesire: String
    let inaltimeCeruta: Int

    init(latime: Int, inaltime: Int, iesire: String) {
        let config = WKWebViewConfiguration()
        let inalt = inaltime > 0 ? inaltime : 900
        vedere = WKWebView(frame: NSRect(x: 0, y: 0, width: latime, height: inalt),
                           configuration: config)
        self.iesire = iesire
        self.inaltimeCeruta = inaltime
        super.init()
        vedere.navigationDelegate = self
    }

    func incarca(_ adresa: String) {
        guard let url = URL(string: adresa) else { exit(2) }
        vedere.load(URLRequest(url: url))
    }

    func webView(_ w: WKWebView, didFinish navigation: WKNavigation!) {
        // fonturile Google se descarca dupa DOMContentLoaded; asteptam sa se aseze
        DispatchQueue.main.asyncAfter(deadline: .now() + 2.2) {
            if self.inaltimeCeruta == 0 {
                w.evaluateJavaScript("document.body.scrollHeight") { rezultat, _ in
                    let h = (rezultat as? CGFloat) ?? 900
                    w.frame = NSRect(x: 0, y: 0, width: w.frame.width, height: max(h, 400))
                    DispatchQueue.main.asyncAfter(deadline: .now() + 1.0) { self.fotografiaza() }
                }
            } else {
                self.fotografiaza()
            }
        }
    }

    func webView(_ w: WKWebView, didFail n: WKNavigation!, withError e: Error) { termina(e) }
    func webView(_ w: WKWebView, didFailProvisionalNavigation n: WKNavigation!, withError e: Error) { termina(e) }

    func termina(_ e: Error) {
        FileHandle.standardError.write("eroare: \(e.localizedDescription)\n".data(using: .utf8)!)
        exit(1)
    }

    func fotografiaza() {
        let config = WKSnapshotConfiguration()
        config.rect = CGRect(origin: .zero, size: vedere.frame.size)
        vedere.takeSnapshot(with: config) { imagine, eroare in
            guard let imagine = imagine,
                  let tiff = imagine.tiffRepresentation,
                  let bitmap = NSBitmapImageRep(data: tiff),
                  let png = bitmap.representation(using: .png, properties: [:]) else {
                FileHandle.standardError.write("captura a esuat: \(eroare?.localizedDescription ?? "?")\n".data(using: .utf8)!)
                exit(1)
            }
            try? png.write(to: URL(fileURLWithPath: self.iesire))
            print("\(self.iesire)  \(Int(self.vedere.frame.width))x\(Int(self.vedere.frame.height))")
            exit(0)
        }
    }
}

let app = NSApplication.shared
app.setActivationPolicy(.accessory)
let fotograf = Fotograf(latime: latime, inaltime: inaltimeCeruta, iesire: iesire)
fotograf.incarca(adresa)
DispatchQueue.main.asyncAfter(deadline: .now() + 45) {
    FileHandle.standardError.write("expirat\n".data(using: .utf8)!)
    exit(1)
}
app.run()
