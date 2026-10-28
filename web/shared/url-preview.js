/* PHP2SHELL local interface prototype — NO network and NO authorization. */
"use strict";
const preview = document.getElementById("preview");
const result = document.getElementById("message");
preview.addEventListener("click", () => {
  const value = document.getElementById("url").value.trim();
  const scope = document.getElementById("scope").value;
  const pages = Number(document.getElementById("pages").value);
  try {
    if (!value || value.length > 2048 || /\s|\\/.test(value)) {
      throw new Error("Adresse invalide ou trop longue.");
    }
    const url = new URL(value);
    if (url.protocol !== "https:" || !url.hostname || url.username ||
        url.password || url.search || url.hash || (url.port && url.port !== "443")) {
      throw new Error("Indiquer une URL HTTPS sans identifiants, requête ou fragment.");
    }
    if (!Number.isInteger(pages) || pages < 1 || pages > 100) {
      throw new Error("Budget de pages hors limites.");
    }
    if (!["public_metadata", "owned_source"].includes(scope)) {
      throw new Error("Portée de demande inconnue.");
    }
    if (scope === "owned_source") {
      result.textContent =
        "Demande P2 : URL saisie, mais mandat et propriété non vérifiés. " +
        "L'analyse du code source reste désactivée.";
    } else {
      result.textContent =
        "Demande P1 : URL saisie (" + url.hostname +
        "), " + pages + " pages proposées. " +
        "Aucune analyse ni validation DNS n'a été effectuée.";
    }
    result.className = "meta ok";
  } catch (_error) {
    result.textContent =
      "Prévisualisation refusée. Vérifier la syntaxe HTTPS et les limites saisies. " +
      "Aucun audit n'a été lancé.";
    result.className = "meta danger";
  }
});
