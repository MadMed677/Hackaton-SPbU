import { applyMiddleware, createStore, compose }    from 'redux';
import thunk                                        from 'redux-thunk';
import reducers                                     from '../settings/_reducers';
import DevTools                                     from '../settings/_devtools';
// import middleware                                from './_middleware';

if ( module.hot ) {
    module.hot.accept('../settings/_reducers', () =>
        store.replaceReducer( require('../settings/_reducers').default )
    );
}

const middleware = compose(
    applyMiddleware(thunk),
    DevTools.instrument()
);

const store = createStore(reducers, {}, middleware);

export default store;