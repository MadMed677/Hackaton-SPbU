import React, { PropTypes }                 from 'react';
import { If, Then, Else }                   from 'react-if';
import cx                                   from 'classnames';
import OffersList                           from './offers-list.react';

class CategoriesNavigation extends React.Component {
    static propTypes = {
        categories: PropTypes.array,
        category: PropTypes.object,
        offers: PropTypes.array,

        setActive: PropTypes.func,
    };

    static defaultProps = {
        categories: [],
        category: {},
    };

    state = {

    };

    shouldComponentUpdate(nextProps, nextState) {
        if ( nextProps.offers.length == 0 ) return true;
        if ( this.props.offers == nextProps.offers ) return false;
        return true;
    }

    constructor() {
        super();
    }

    _handleClick = (category ,e) => {
        e.preventDefault();

        this.props.setActive(category);
    };

    render() {
        const categories = this.props.categories.map( category => {
            const classes = cx({
                'panel': true,
                'panel-default': category.id != this.props.category.id,
                'panel-primary': category.id == this.props.category.id
            });

            return (
                <div key={`category-${category.id}`} href="#" className={ classes } onClick={ this._handleClick.bind(null, category) }>
                    <div className="panel-heading">{ category.name.toUpperCase() }</div>

                    <If condition={ this.props.category.id == category.id }>
                        <Then>
                            <OffersList offers={ this.props.offers } />
                        </Then>
                    </If>
                </div>
            )
        });

        return (
            <div>
                { categories }
            </div>
        );
    }
}

export default CategoriesNavigation;
