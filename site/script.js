const revealItems = document.querySelectorAll('.reveal');
const soundToggle = document.querySelector('.sound-toggle');
let audioContext;
let soundEnabled = false;

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.14 });

revealItems.forEach((item) => revealObserver.observe(item));

function forgeTone(frequency = 220, duration = 0.08) {
  if (!soundEnabled) return;
  audioContext ??= new (window.AudioContext || window.webkitAudioContext)();
  const oscillator = audioContext.createOscillator();
  const gain = audioContext.createGain();
  oscillator.type = 'sine';
  oscillator.frequency.setValueAtTime(frequency, audioContext.currentTime);
  oscillator.frequency.exponentialRampToValueAtTime(frequency * 1.8, audioContext.currentTime + duration);
  gain.gain.setValueAtTime(0.0001, audioContext.currentTime);
  gain.gain.exponentialRampToValueAtTime(0.045, audioContext.currentTime + 0.01);
  gain.gain.exponentialRampToValueAtTime(0.0001, audioContext.currentTime + duration);
  oscillator.connect(gain).connect(audioContext.destination);
  oscillator.start();
  oscillator.stop(audioContext.currentTime + duration + 0.02);
}

soundToggle?.addEventListener('click', () => {
  soundEnabled = !soundEnabled;
  soundToggle.setAttribute('aria-pressed', String(soundEnabled));
  soundToggle.textContent = soundEnabled ? 'Sound on' : 'Sound off';
  if (soundEnabled) forgeTone(180, 0.14);
});

document.querySelectorAll('.forge-sound').forEach((element) => {
  element.addEventListener('mouseenter', () => forgeTone(260, 0.055));
  element.addEventListener('click', () => forgeTone(380, 0.1));
});
