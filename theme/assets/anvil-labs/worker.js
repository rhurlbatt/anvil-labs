(()=>{var i=()=>{throw new Error("not implemented")};function e(t,n){if(t.startsWith("app/")){let s=Sk.builtinFiles.files;s[t]=n;let[a,r]=t.split("/");s[`app/${r}/__init__.py`]??="pass"}return n}function o(t){let n=i(t);return n instanceof Sk.misceval.Suspension?Sk.misceval.promiseToSuspension(Sk.misceval.asyncToPromise(()=>n).then(s=>e(t,s))):e(t,n)}Object.defineProperty(Sk,"read",{get(){return o},set(t){i=t},configurable:!0});})();
