package None;

import java.util.List;
import lombok.*;



/* version: 0.3.0.post26.dev0+e73dc8d */


/**
  A base class for all types of related identifiers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RelatedIdentifier  {

  private String type;

}
