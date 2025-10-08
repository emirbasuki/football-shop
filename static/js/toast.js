function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastIcon = document.getElementById('toast-icon');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');

    // set content
    toastTitle.textContent = title || '';
    toastMessage.textContent = message || '';

    // set icon / color by type
    toastIcon.textContent = '';
    toastComponent.classList.remove('bg-green-50','bg-red-50','bg-yellow-50','text-green-600','text-red-600');
    if (type === 'success') {
        toastIcon.textContent = '✔️';
        toastComponent.classList.add('bg-green-50');
    } else if (type === 'error') {
        toastIcon.textContent = '⚠️';
        toastComponent.classList.add('bg-red-50');
    } else if (type === 'warn') {
        toastIcon.textContent = '⚠️';
        toastComponent.classList.add('bg-yellow-50');
    }

    // show
    toastComponent.classList.remove('translate-y-64', 'opacity-0');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    // hide after duration
    clearTimeout(window.__toast_hide_timeout);
    window.__toast_hide_timeout = setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}


// showConfirmToast: returns Promise<boolean>
function showConfirmToast(title, message, confirmLabel = 'Confirm', cancelLabel = 'Cancel') {
    return new Promise((resolve) => {
        // create container
        const container = document.createElement('div');
        container.className = 'fixed bottom-8 right-8 z-50 p-4 px-6 rounded-xl shadow-xl bg-white border border-gray-200 flex items-start gap-4 max-w-sm';

        container.innerHTML = `
            <div class="flex-0 text-2xl">❗</div>
            <div class="flex-1">
              <h3 class="font-bold mb-1">${escapeHtml(title || '')}</h3>
              <p class="text-sm text-gray-700 mb-3">${escapeHtml(message || '')}</p>
              <div class="flex gap-2 justify-end">
                <button id="toast-cancel" class="px-3 py-1 rounded-md bg-gray-100 text-gray-700">${escapeHtml(cancelLabel)}</button>
                <button id="toast-confirm" class="px-3 py-1 rounded-md bg-red-600 text-white">${escapeHtml(confirmLabel)}</button>
              </div>
            </div>
        `;

        document.body.appendChild(container);

        // entrance animation
        container.style.transform = 'translateY(20px)';
        container.style.opacity = '0';
        requestAnimationFrame(() => {
            container.style.transition = 'all 180ms ease';
            container.style.transform = 'translateY(0)';
            container.style.opacity = '1';
        });

        function cleanup() {
            container.style.transform = 'translateY(20px)';
            container.style.opacity = '0';
            setTimeout(() => container.remove(), 200);
        }

        const btnConfirm = container.querySelector('#toast-confirm');
        const btnCancel = container.querySelector('#toast-cancel');

        btnConfirm.addEventListener('click', () => {
            cleanup();
            resolve(true);
        });

        btnCancel.addEventListener('click', () => {
            cleanup();
            resolve(false);
        });

        // if user clicks outside (optional) -> cancel
        const onKey = (e) => {
            if (e.key === 'Escape') {
                cleanup();
                resolve(false);
                document.removeEventListener('keydown', onKey);
            }
        };
        document.addEventListener('keydown', onKey);
    });
}

// small helper to prevent XSS when injecting text
function escapeHtml(unsafe) {
    return String(unsafe)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
}