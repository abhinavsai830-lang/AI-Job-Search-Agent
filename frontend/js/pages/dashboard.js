import { apiFetch } from "../api.js";

async function loadHealthStatus() {
  try {
    const data = await apiFetch("/health");
    const chip = document.querySelector(".status-chip");
    if (chip && data.status === "healthy") {
      chip.textContent = "API healthy";
    }
  } catch (error) {
    const chip = document.querySelector(".status-chip");
    if (chip) {
      chip.textContent = "API offline";
    }
    console.error(error);
  }
}

loadHealthStatus();
