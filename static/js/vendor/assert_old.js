/**
 * Bundled by jsDelivr using Rollup v2.79.2 and Terser v5.39.0.
 * Original file: /npm/@noble/hashes@1.7.1/esm/_assert.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
function e(e){if(!Number.isSafeInteger(e)||e<0)throw new Error("positive integer expected, got "+e)}function t(e,...t){if(!((r=e)instanceof Uint8Array||ArrayBuffer.isView(r)&&"Uint8Array"===r.constructor.name))throw new Error("Uint8Array expected");var r;if(t.length>0&&!t.includes(e.length))throw new Error("Uint8Array expected of length "+t+", got length="+e.length)}function r(t){if("function"!=typeof t||"function"!=typeof t.create)throw new Error("Hash should be wrapped by utils.wrapConstructor");e(t.outputLen),e(t.blockLen)}function n(e,t=!0){if(e.destroyed)throw new Error("Hash instance has been destroyed");if(t&&e.finished)throw new Error("Hash#digest() has already been called")}function o(e,r){t(e);const n=r.outputLen;if(e.length<n)throw new Error("digestInto() expects output buffer of length at least "+n)}export{t as abytes,n as aexists,r as ahash,e as anumber,o as aoutput};export default null;
//# sourceMappingURL=/sm/30a69dc264e1bf8f5cfcc137e1928cb51f235a767875ae0fcd33d2675477d5d8.map